val lines = """5 5 2 2 3
2 2
3 2
3 3
4 1
1 4""".split('\n')
var ln = 0

fun readln(): String {
    ln += 1
    return lines[ln - 1]
}

fun main() {
	val segments = readln().split(' ').map { it.toInt() }
    val xsize = segments[0]
    val ysize = segments[1]
    val xext = segments[2]
    val yext = segments[3]
    val obsCount = segments[4]
    
    val world = List(xsize) { BooleanArray(ysize) { true } }
    repeat(obsCount) {
        val (ox, oy) = readln().split(' ').map { it.toInt() - 1 }
        world[ox][oy] = false
    }
    
    val (sx, sy) = readln().split(' ').map { it.toInt() - 1 }
    val (ex, ey) = readln().split(' ').map { it.toInt() - 1 }
    
    fun isPassable(px: Int, py: Int): Boolean {
        for (x in px until px + xext) {
            for (y in py until py + yext) {
                if (world.getOrNull(x)?.getOrNull(y)?:false == false) {
                    return false
                }
            }
        }
        return true
    }
    
    if (!isPassable(sx, sy)) {
        println(-1)
        return
    }
    
    val visited = List(xsize) { IntArray(ysize) { -1 } }
    val toVisit = ArrayDeque<Pair<Int, Int>>()
    
    visited[sx][sy] = 0
    toVisit.addLast(Pair(sx, sy))
    
    while (toVisit.isNotEmpty()) {
        val (vx, vy) = toVisit.removeFirst()
        // println("visited $vx $vy")
        
        for ((wx, wy) in listOf(
        	Pair(vx+1, vy),
            Pair(vx-1, vy),
            Pair(vx, vy+1),
            Pair(vx, vy-1),
        )) {
			// println("visited $vx $vy -- route $wx $wy")
            if (isPassable(wx, wy) && visited[wx][wy] == -1) {
                // println("visited $vx $vy -- route $wx $wy -- passable")
                visited[wx][wy] = visited[vx][vy] + 1
                toVisit.addLast(Pair(wx, wy))
                
                if (wx == ex && wy == ey) {
                    println(visited[wx][wy])
                    return
                }
            }
        }
    }
    
    println(-1)
    return
}
