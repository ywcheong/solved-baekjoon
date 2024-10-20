// My Solution : https://github.com/ywcheong/solved-baekjoon

// Header
// FILL HERE: Import External Library

private var TESTCASE_ID = 1
private fun <T> equal(left: T, right: T) {
    if (left == right) {
        println("Testcase $TESTCASE_ID: OK ($left == $right)")
    } else {
        println("Testcase $TESTCASE_ID: FAIL ($left != $right)")
    }
    TESTCASE_ID++
}

// Implementation
// FILL HERE: Implement
private fun getAdd(a: Int, b: Int): Int {
    return a + b
}

// Testing
private fun test() {
    println("WARNING: TEST MODE")

    // FILL HERE: Write Testcases
    equal(getAdd(3, 4), 7)
    equal(getAdd(5, 6), 11)

    println("TEST DONE")
}

// Submit
private fun submit() {
    // FILL HERE: Get Inputs
    val (a, b) = readln().split(" ").map{ it.toInt() }
    println(getAdd(a, b))
}

// Case-switch
fun main() {
    // test()
    submit()
}