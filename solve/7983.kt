import kotlin.math.*

// val lines = """1
// 2 8""".split('\n')
// var lineNo = 0

// fun readln(): String = lines[lineNo++]

fun solve(taskDates: IntArray, dueDates: IntArray, size: Int): Int {
    // println("given: taskDates ${taskDates.asList()} dueDates ${dueDates.asList()} size $size")
    val indicies = IntArray(size) { it }.sortedBy { -dueDates[it] }
    
    var thisWorkMayEndAt = Int.MAX_VALUE
    for (index in indicies) {
        thisWorkMayEndAt = min(thisWorkMayEndAt, dueDates[index]) - taskDates[index]
    }
    
    return thisWorkMayEndAt
}

fun main() {
    val size = readln().toInt()
    val taskDates = IntArray(size) { -1 }
    val dueDates = IntArray(size) { -1 }
    
    for (i in 0 ..< size) {
        val (taskDate, dueDate) = readln().split(' ').map { it.toInt() }
        taskDates[i] = taskDate
        dueDates[i] = dueDate
    }
    
    println(solve(taskDates, dueDates, size))
}
