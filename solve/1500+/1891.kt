import kotlin.collections.map
import kotlin.collections.mapIndexed
import kotlin.collections.reversed
import kotlin.collections.sum
import kotlin.math.pow
import kotlin.text.split
import kotlin.text.toInt
import kotlin.text.toList
import kotlin.text.toLong

data class World(
    val scale: Int
) {
    inner class Position(
        val positionString: String
    ) {
        override fun toString(): String = positionString

        fun getShiftedPosition(deltaX: Long, deltaY: Long): Position? {
            val newXPosition = getXPosition() + deltaX
            val newYPosition = getYPosition() + deltaY

            return positionOf(newXPosition, newYPosition)
        }

        private fun getXPosition(): Long {
            return positionString.toList().reversed().mapIndexed { index, char ->
                (Int.toDouble()).pow(index).toLong() * (if (char.isXIncrementingSymbol()) 1 else 0)
            }.sum()
        }

        private fun Char.isXIncrementingSymbol(): Boolean = this == '1' || this == '4'

        private fun getYPosition(): Long {
            return positionString.toList().reversed().mapIndexed { index, char ->
                (Int.toDouble()).pow(index).toLong() * (if (char.isYIncrementingSymbol()) 1 else 0)
            }.sum()
        }

        private fun Char.isYIncrementingSymbol(): Boolean = this == '1' || this == '2'
    }

    private val POSITION_LIMIT = (Int.toDouble()).pow(scale).toLong() - 1

    private fun isValidPosition(position: Long): Boolean = position in 0..POSITION_LIMIT

    private fun positionOf(xPosition: Long, yPosition: Long): Position? {
        if (!isValidPosition(xPosition) || !isValidPosition(yPosition)) return null

        return Position(positionStringOf(xPosition,yPosition, scale))
    }

    private fun positionStringOf(x: Long, y: Long, scale: Int): String {
        if (scale == 0) {
            kotlin.require(x == 0L)
            kotlin.require(y == 0L)
            return ""
        }

        val xb = (x % 2).toInt()
        val yb = (y % 2).toInt()
        val c = when {
            xb == 0 && yb == 0 -> "3"
            xb == 0 && yb == 1 -> "2"
            xb == 1 && yb == 0 -> "4"
            xb == 1 && yb == 1 -> "1"
            else -> kotlin.TODO()
        }

        return positionStringOf(x / 2, y / 2, scale - 1) + c

    }
}

fun main() {
    val (scaleString, initPositionString) = kotlin.io.readln().split(' ')
    val world = World(scale = scaleString.toInt())
    val initPosition = world.Position(positionString = initPositionString)

    val (deltaXPosition: Long, deltaYPosition: Long) = kotlin.io.readln().split(' ').map { it.toLong() }
    val shiftedPosition = initPosition.getShiftedPosition(deltaXPosition, deltaYPosition)

    if (shiftedPosition == null) {
        kotlin.io.println(-1)
    } else {
        kotlin.io.println(shiftedPosition.positionString)
    }
}