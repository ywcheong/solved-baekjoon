// val lines = """6 3
// 1 2
// 2 3
// 3 4
// 6 5
// 1 2
// 2 3
// 3 4
// 4 5
// 5 6
// 6 6
// 1 2
// 2 3
// 1 3
// 4 5
// 5 6
// 6 4
// 0 0""".split('\n')
// var ln = 0

// fun readln(): String {
//     ln += 1
//     return lines[ln - 1]
// }

fun readTwoInt() = readln().split(' ').map { it.toInt() }

fun main() {
    var caseId = 1
    while (true) {
        // ============= Judging
        val (nodeSize, edgeSize) = readTwoInt()
        if (nodeSize == 0 && edgeSize == 0) break
        
        // ============= Preparing
        val edges = List(nodeSize) { mutableListOf<Int>() }
        repeat(edgeSize) {
            val (vr, wr) = readTwoInt()
            val v = vr - 1
            val w = wr - 1
            edges[v].add(w)
            edges[w].add(v)
        }
        
        // ============= Solving
        val visited = IntArray(nodeSize) { -1 }
        val parent = IntArray(nodeSize) { -1 }
        val toVisit = ArrayDeque<Int>()
        var treeNums = 0
        
        for (start in 0 until nodeSize) {
            if (visited[start] != -1) continue // already visited
            
            // println("-- starting from $start")
            
            visited[start] = start // set groupId as itself
            toVisit.addLast(start) // and prepare to start
            var isTree = true
            
            while (toVisit.isNotEmpty()) {
                val v = toVisit.removeFirst() // bfs
                // println("-- starting from $start, visiting $v")
                
                for (w in edges[v]) {
                    // println("-- starting from $start, visiting $v, routing $w")
                    
                    if (parent[v] == w) {
                        // println("-- starting from $start, visiting $v, routing $w, but parent skip")
                        continue
                    }
                    
                    if (visited[w] == -1) {
                        // not visited yet - ok
                        // println("-- starting from $start, visiting $v, routing $w, not visited")
                        visited[w] = start
                        parent[w] = v
                        toVisit.addLast(w)
                    } else if (visited[w] == start) {
                        // visited, means loop detected
                        // println("-- starting from $start, visiting $v, routing $w, visited")
                        isTree = false
                    } else {
                        // PREVIOUS LOOP COLLISON -> logically impossible
                        TODO("what? impossible")
                    }
                }
            } // end while (toVisit.isNotEmpty())
            
            if (isTree) treeNums += 1
            
        } // end for (start in 0 until nodeSize)
        
        val message = when (treeNums) {
            0 -> "No trees."
            1 -> "There is one tree."
            else -> "A forest of $treeNums trees."
        }
        
        println("Case $caseId: $message")
        caseId += 1
        
    } // end of while (true)
}
