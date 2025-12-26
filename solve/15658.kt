// val lines = """6
// 1 2 3 4 5 6
// 3 2 1 1""".split('\n')
// var lineNo = 0

// fun readln(): String {
//     lineNo += 1
//     return lines[lineNo - 1]
// }

const val ADD_INDEX = 0
const val SUB_INDEX = 1
const val MUL_INDEX = 2
const val DIV_INDEX = 3

fun max(a: Int, b: Int) = when (a > b) {
    true -> a
    false -> b
}

fun min(a: Int, b: Int) = when (a > b) {
    true -> b
    false -> a
}

fun main() {
    val size = readln().toInt()
    val nums = readln().split(' ').map { it.toInt() }
    val remainOps = readln().split(' ').map { it.toInt() }.toMutableList()
    
    val accs = IntArray(size) { 987654321 }.apply {
        this[0] = nums[0]
    }
    
    var resultMin = Int.MAX_VALUE
    var resultMax = Int.MIN_VALUE
    
    fun updateResult(x: Int) {
        resultMax = max(resultMax, x)
        resultMin = min(resultMin, x)
    }
    
    fun backtrack(index: Int) {
        
        // println("backtrack($index) = MINMAX[$resultMin ~ $resultMax] ACC $accs OP# $remainOps")
        
        // terminal
        if (index == size - 1) {
            updateResult(accs[index])
            return
        }
        
        for (opidx in 0..3) {
            if (remainOps[opidx] == 0) continue
            
            // push
            remainOps[opidx] -= 1
            
            // op ( acc[i] , num[i+1] ) ->acc[i+1]
            when (opidx) {
                ADD_INDEX -> {
                    accs[index + 1] = accs[index] + nums[index + 1]
                }
                
                SUB_INDEX -> {
                    accs[index + 1] = accs[index] - nums[index + 1]
                }
                
                MUL_INDEX -> {
                    accs[index + 1] = accs[index] * nums[index + 1]
                }
                
                DIV_INDEX -> {
                    accs[index + 1] = accs[index] / nums[index + 1]
                }
                
                else -> TODO("???")
            }
            
            // backtrack
            backtrack(index + 1)
            
            // pop
            remainOps[opidx] += 1
        }
    }
    
    backtrack(0)
    
    println(resultMax)
    println(resultMin)
}
