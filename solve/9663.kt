/*
    !!! THIS IS CHATGPT-GENERATED CODE !!!

    Prompt:
        Convert 9663.py to 9663.kt (Kotlin). The content of 9663.py is as the following.

        ```
        (9663.py content)
        ```
*/

import kotlin.system.measureTimeMillis

var TESTCASE_ID = 1

fun equal(left: Int, right: Int) {
    if (left == right) {
        println("Testcase $TESTCASE_ID: OK ($left == $right)")
    } else {
        println("Testcase $TESTCASE_ID: FAIL ($left != $right)")
    }
    TESTCASE_ID++
}

fun solveQueen(n: Int): Int {
    var result = 0

    fun isValid(queens: IntArray, level: Int, column: Int): Boolean {
        for (oldLevel in 0 until level) {
            val oldColumn = queens[oldLevel]
            if (column == oldColumn || (level - oldLevel) == Math.abs(column - oldColumn)) {
                return false
            }
        }
        return true
    }

    fun backtrack(queens: IntArray, level: Int) {
        if (level == n) {
            result++
            return
        }

        for (column in 0 until n) {
            if (isValid(queens, level, column)) {
                queens[level] = column
                backtrack(queens, level + 1)
            }
        }
    }

    backtrack(IntArray(n) { -1 }, 0)
    return result
}

fun test() {
    println("WARNING: TEST MODE")

    equal(solveQueen(1), 1)
    equal(solveQueen(2), 0)
    equal(solveQueen(3), 0)
    equal(solveQueen(4), 2)
    equal(solveQueen(8), 92)
    println(solveQueen(14))

    val executionTime = measureTimeMillis {
        solveQueen(14)
    }
    println("Execution time for N=14: $executionTime ms")

    println("TEST DONE")
}

fun submit() {
    val n = readLine()!!.toInt()
    println(solveQueen(n))
}

fun main() {
    test()
}
