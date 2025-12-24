// val lines = """abcd
// 3
// P x
// L
// P y""".split('\n')
// var lineNum = 0

// fun readln(): String {
//     lineNum += 1
//     return lines[lineNum - 1]
// }

class Node(
	var left: Node?,
    var right: Node?,
    val value: Char,
) {
    override fun toString() = if (right == null) "$value" else "$value$right"
    
    fun isHead() = value == HEAD.value
    fun isTail() = value == TAIL.value
    
    fun pop() {
        left?.also {
            it.right = this.right
        }
        
        right?.also {
            it.left = this.left
        }
        
        left = null
        right = null
    }
    
    fun insertRight(other: Node) {
        val mid = other
        val left = this
        val right = this.right
        
        if (right == null) {
            left.right = mid
            mid.left = left
            return
        }
        
        insert(left, mid, right)
    }
    
    fun insertLeft(other: Node) {
        val mid = other
        val left = this.left
        val right = this
        
        if (left == null) {
            mid.right = right
            right.left = mid
            return
        }
        
        insert(left, mid, right)
    }
    
    companion object {
        val HEAD = from('[')
        val TAIL = from(']')
        
        fun from(value: Char) = Node(
        	left = null,
            right = null,
            value = value,
        )
        
        fun insert(left: Node, mid: Node, right: Node) {
            left.right = mid
            mid.left = left
            mid.right = right
            right.left = mid
        }
    }
}

fun main() {
    val nodeList = readln().toList().map { Node.from(it) }
    (0 until nodeList.size).forEach { index ->
        val leftNode = nodeList.getOrNull(index - 1) ?: Node.HEAD
        val rightNode = nodeList.getOrNull(index + 1) ?: Node.TAIL
        nodeList[index].apply {
            left = leftNode
            right = rightNode
        }
    }
    
    Node.HEAD.right = nodeList.first()
    Node.TAIL.left = nodeList.last()
    
    val cursor = Node.from('|')
    Node.TAIL.insertLeft(cursor)
    
    val commandCount = readln().toInt()
    // println("init :: ${Node.HEAD}")
    repeat (commandCount) {
        val command = readln()
        if (command == "L") {
            if (cursor.left != Node.HEAD) {
                val newRight = cursor.left!!
                cursor.pop()
                newRight.insertLeft(cursor)
            }
        } else if (command == "D") {
            if (cursor.right != Node.TAIL) {
                val newLeft = cursor.right!!
                cursor.pop()
                newLeft.insertRight(cursor)
            }
        } else if (command == "B") {
            if (cursor.left != Node.HEAD) {
                cursor.left!!.pop()
            }
        } else {
            val newCharNode = Node.from(command[2])
            cursor.insertLeft(newCharNode)
        }
        // println("$it :: ${Node.HEAD}")
    }
    
    cursor.pop()
    
    val result = buildString {
        var current = Node.HEAD.right!!
    	while (current != Node.TAIL) {
        	append(current.value)
        	current = current.right!!
    	}
    }
    
    println(result)
}
