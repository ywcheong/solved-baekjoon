const val USED = 0
const val NOT_USED = 1

fun solve(size: Int, isUsed: MutableList<IntArray>, world: List<String>): Int {
    for (top in 0 until size) {
        for (left in 0 .. top) {
            if (isUsed[top][left] == NOT_USED) {
                when (world[top][left]) {
                    'R' -> {
                        // Greedy: this forces [t,l], [t+1,l], [t+1,l+1] to be B and used
                        if (world.getOrNull(top + 1)?.getOrNull(left) == 'R'
                            && isUsed.getOrNull(top + 1)?.getOrNull(left) == NOT_USED
                            && world.getOrNull(top + 1)?.getOrNull(left + 1) == 'R'
                            && isUsed.getOrNull(top + 1)?.getOrNull(left + 1) == NOT_USED
                        ) {
                            isUsed[top][left] = USED
                            isUsed[top + 1][left] = USED
                            isUsed[top + 1][left + 1] = USED
                        } else {
                            return 0
                        }
                    }

                    'B' -> {
                        // Greedy: this forces [t,l], [t,l+1], [t+1,l+1] to be B and used
                        if (world.getOrNull(top)?.getOrNull(left + 1) == 'B'
                            && isUsed.getOrNull(top)?.getOrNull(left + 1) == NOT_USED
                            && world.getOrNull(top + 1)?.getOrNull(left + 1) == 'B'
                            && isUsed.getOrNull(top + 1)?.getOrNull(left + 1) == NOT_USED
                        ) {
                            isUsed[top][left] = USED
                            isUsed[top][left + 1] = USED
                            isUsed[top + 1][left + 1] = USED
                        } else {
                            return 0
                        }
                    }

                    else -> return 0
                }
            }
        }
    }

    return 1
}

fun main() {
    val size = readln().toInt()
    val world: List<String> = List(size) { readln() }
    val isUsed = MutableList(size) { index ->
        IntArray(world[index].length) { NOT_USED }
    }

    println(solve(size, isUsed, world))
}
