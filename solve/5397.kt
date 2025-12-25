class Node(
	val stroke: Char?,
    var left: Node?,
    var right: Node?,
) {
    fun insertLeft(newLeft: Node) {
        if (left == null) {
            this.left = newLeft
            newLeft.right = this
            return
        }
        
        link(this.left!!, newLeft, this)
    }
    
    fun insertRight(newRight: Node) {
        if (right == null) {
            this.right = newRight
            newRight.left = this
            return
        }
        
        link(this, newRight, this.right!!)
    }
    
    fun popThis(): Node {
        left?.also {
            it.right = right
        }
        
        right?.also {
            it.left = left
        }
        
        left = null
        right = null
        
        return this
    }
    
    companion object {        
        fun from(stroke: Char?) = Node(stroke = stroke, left = null, right = null)
        fun link(left: Node, mid: Node, right: Node) {
            left.right = mid
            mid.left = left
            mid.right = right
            right.left = mid
        }
    }
}

fun main() {
    val testcaseNum = readln().toInt()
    repeat(testcaseNum) { _unused ->
        val HEAD = Node.from(null)
        val cursor = Node.from(null)
        val TAIL = Node.from(null)
        
        Node.link(HEAD, cursor, TAIL)
        
        readln().forEach { stroke ->
            when (stroke) {
                '>' -> {
                    if (cursor.right != TAIL) {
                        val right = cursor.right!!.popThis()
                        cursor.insertLeft(right)
                    }
                }
                
                '<' -> {
                    if (cursor.left != HEAD) {
                        val left = cursor.left!!.popThis()
                        cursor.insertRight(left)
                    }
                }
                
                '-' -> {
                    if (cursor.left != HEAD) {
                        cursor.left!!.popThis()
                    }
                }
                
                else -> {
                    val strokeNode = Node.from(stroke)
                    cursor.insertLeft(strokeNode)
                }
            }
            
        } // end of readln foreach
        
        // remove cursor
        cursor.popThis()
        
        // print result
        val result = buildString {
            var printCursor = HEAD.right!!
            while (printCursor != TAIL) {
                append(printCursor.stroke!!)
                printCursor = printCursor.right!!
            }
        }
        
        println(result)
        
    } // end of repeat
}
