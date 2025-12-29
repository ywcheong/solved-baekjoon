import kotlin.math.*

val lines = """8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0""".split('\n')
var lineNo = 0
fun readln(): String = lines[lineNo++]

fun readInts(): List<Int> = readln().split(' ').map { it.toInt() }

data class Shortcut(
	val start: Int,
    val end: Int,
    val length: Int,
)

fun main() {
    val (shortcutSize, roadLength) = readInts()
    val shortcuts = List(shortcutSize) {
        val (start, end, length) = readInts()
        Shortcut(start, end, length)
    }.filter { it.end <= roadLength }.sortedBy { it.start }
    
    /**
     * first, compute NearestStart for each end (assert length of distance as start)
     * then, result = Map<Pos, Len>
     * result[first start] = start
     * 
     * for each start of shortcut:
     * 		find (len) of result[start]
     *      find next start, using normal driving ** (multiple start can collide)
     * 		find end of start, using shortcut
     * 		try put two thing:
     * 			(start's next start, len + (next start - start))
     * 			(end's next start, len + (shortcut length) + (next start - end))				
     */
     
     val findNextStartGeThan = { pos: Int ->
         shortcuts.filter { it.start > pos }.minByOrNull { it.start }?.start ?: roadLength
     } // TODO this might be optimized further
     
     val findNextStartGeqThan = { pos: Int ->
         shortcuts.filter { it.start >= pos }.minByOrNull { it.start }?.start ?: roadLength
     } // TODO this might be optimized further
     
     val findAllByStart = { start: Int ->
     	shortcuts.filter { it.start == start }
     } // TODO this might be optimized further
     
     val firstStart = shortcuts.minByOrNull { it.start }?.start ?: 0
     
     val result = mutableMapOf<Int, Int>().apply {
         tryPut(firstStart, firstStart)
         tryPut(roadLength, roadLength)
     }
     
     val starts = shortcuts.map { it.start }.sorted().distinct()
     for (start in starts) {
         val currentDistance = result[start]!!
//          println("start = $start (dist $currentDistance)")
         
         run {
         	val nextStart = findNextStartGeThan(start)
         	result.tryPut(nextStart, currentDistance + (nextStart - start))
         }
         
         for (shortcut in findAllByStart(start)) {
             val nextStart = findNextStartGeqThan(shortcut.end)
             result.tryPut(nextStart, currentDistance + (nextStart - shortcut.end + shortcut.length))
         }
     }
     
     println(result[roadLength]!!)
}

fun MutableMap<Int, Int>.tryPut(key: Int, value: Int) {
    // println("RESULT[$key] <- before ${this[key]}, try $value")
    this[key] = min(this[key] ?: Int.MAX_VALUE, value)
}
