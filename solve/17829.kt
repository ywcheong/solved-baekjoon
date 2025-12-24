fun secondOf(a: Int, b: Int, c: Int, d: Int): Int {
    return listOf(a, b, c, d).sorted()[2]
}

fun main() {
    val size = readln().toInt()
    val world: MutableList<MutableList<Int>> = MutableList(size) {
        readln().split(' ').map { it.toInt() }.toMutableList()
    }
    
//     val size = 4
//     val world = mutableListOf(
//         mutableListOf(-6, -8, 7, -4),
//         mutableListOf(-5, -5, 14, 11),
//         mutableListOf(11, 11, -1, -1),
//         mutableListOf(4, 9, -2, -4),
//     )
    
    fun pool(scale: Int) {
        val twoScale = scale * 2
        (0 until size step twoScale).forEach { x ->
            (0 until size step twoScale).forEach { y ->
                world[x][y] = secondOf(
                    world[x][y],
                    world[x + scale][y],
                    world[x][y + scale],
                    world[x + scale][y + scale],
                )
            }
        }
    }
    
    var poolSize = 1
    while (poolSize < size) {
        pool(poolSize)
        poolSize *= 2
    }
    
    println(world[0][0])
}
