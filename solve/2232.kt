// val lines = """9
// 1
// 2
// 5
// 4
// 3
// 3
// 6
// 6
// 2""".split('\n')
// var lineNo = 0

// fun readln(): String {
//     return lines[lineNo++]
// }

fun solve(nums: IntArray, size: Int): String = buildString {
    var pos = 0
    while (pos < size) {
        // find next highest -> count it
        // println("++ phase :: pos $pos")
        while ((pos + 1 < size) && (nums[pos] < nums[pos + 1])) {
        	pos++
            // println("++ phase :: pos $pos")
    	}
        
        // println("++ phase stop :: pos $pos")
        
        appendLine(pos + 1)
    	if (pos == size - 1) break
        
        // println("-- phase :: pos $pos")
        
        // enjoy decrease
        while ((pos + 1 < size) && (nums[pos] > nums[pos + 1])) {
            pos++
            // println("-- phase :: pos $pos")
        }
        
        if (pos == size - 1) break
        pos++
    }
}

fun main() {
    val size = readln().toInt()
    val nums = IntArray(size) { readln().toInt() }
    
    println(solve(nums, size))
}
