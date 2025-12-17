data class World(
    val height: Int, val width: Int, val isConductable: List<List<Boolean>>
) {
    inner class Position(
        val h: Int, val w: Int
    ) {
        override fun toString() = "Pos[h=$h w=$w isCon=${isConductablePosition()} isTer=${isTerminatingPosition()}]"

        init {
            require(h in 0..<height)
            require(w in 0..<width)
        }

        fun isConductablePosition(): Boolean = isConductable[h][w]

        fun getAdjacentConductablePosition(): List<Position> = listOfNotNull(
            posOf(h + 1, w), posOf(h - 1, w), posOf(h, w + 1), posOf(h, w - 1)
        ).filter { it.isConductablePosition() }

        fun isTerminatingPosition(): Boolean = (h == height - 1)
    }

    fun posOf(h: Int, w: Int): Position? {
        return if (h in 0..<height && w in 0..<width) Position(h, w) else null
    }

    fun isPercolatable(): Boolean {
        val visitedPositionMap: MutableList<MutableList<Boolean>> = MutableList(height) {
            MutableList(width) { false }
        }
        val toVisitPositions: ArrayDeque<Position> =
            ArrayDeque((0..<width).map { w -> Position(h = 0, w = w) }.filter { it.isConductablePosition() })

        while (toVisitPositions.isNotEmpty()) {
            val currentPos = toVisitPositions.removeFirst()
            // println("current: $currentPos")
            visitedPositionMap.markAsVisited(currentPos)

            for (nextPos in currentPos.getAdjacentConductablePosition()) {
                if (!visitedPositionMap.isVisited(nextPos)) {
                    // println("--- next: $nextPos")
                    if (nextPos.isTerminatingPosition()) return true

                    visitedPositionMap.markAsVisited(nextPos)
                    toVisitPositions.add(nextPos)
                }
            }
        }

        return false
    }

    fun MutableList<MutableList<Boolean>>.isVisited(pos: Position): Boolean = this[pos.h][pos.w]
    fun MutableList<MutableList<Boolean>>.markAsVisited(pos: Position) {
        this[pos.h][pos.w] = true
    }
}

fun main() {
    val (height: Int, width: Int) = readln().split(' ').map { it.toInt() }
    val isConductable: List<List<Boolean>> = List(height) {
        readln().toList().map { it == '0' }
    }

    val world = World(
        height = height, width = width, isConductable = isConductable
    )

    when (world.isPercolatable()) {
        true -> println("YES")
        false -> println("NO")
    }
}