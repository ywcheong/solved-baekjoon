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


// Testing
private fun test() {
    println("WARNING: TEST MODE")

    // FILL HERE: Write Testcases

    println("TEST DONE")
}

// Submit
private fun submit() {
    // FILL HERE: Get Inputs
}

// Case-switch
fun main() {
    test()
    submit()
}