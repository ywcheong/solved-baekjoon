fun max(a: Int, b: Int): Int = when (a > b) {
    true -> a
    false -> b
}

fun main() {
    val (size, blackUpperBound, whiteLowerBound) = readln().split(' ').map { it.toInt() }
    val world = readln()
    
    var answer = 0
    var start = 0; var end = 0;
    var blackCount = 0; var whiteCount = 0;
    
    fun increment() {
        when (world[end]) {
            'B' -> blackCount += 1
            'W' -> whiteCount += 1
            else -> TODO()
        }
        end += 1
    }
    
    fun decrement() {
        when (world[start]) {
            'B' -> blackCount -= 1
            'W' -> whiteCount -= 1
            else -> TODO()
        }
        start += 1
    }
    
    while (true) {
        // println("start $start ~ end $end // w $whiteCount b $blackCount")
        if (end < size && whiteCount < whiteLowerBound) {
            increment()
            continue
        }
        
        if (start < size && blackCount > blackUpperBound) {
        	decrement()
        	continue
        }
        
        if (whiteCount < whiteLowerBound || blackCount > blackUpperBound) break
        
        answer = max(answer, end - start)
        if (end == size) break
        else increment()
    }
    
    println(answer)
}
