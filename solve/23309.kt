import java.util.StringTokenizer
import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

class MapNodes(
    val nexts: IntArray,
    val prevs: IntArray,
) {
    fun pop(some: Int) {
        prevs[nexts[some]] = prevs[some]
        nexts[prevs[some]] = nexts[some]

        prevs[some] = -1
        nexts[some] = -1
    }

    fun insertNext(some: Int, other: Int) {
        val _prev = some
        val _mid = other
        val _next = nexts[some]

        insert(_prev, _mid, _next)
    }

    fun insertPrev(some: Int, other: Int) {
        val _prev = prevs[some]
        val _mid = other
        val _next = some

        insert(_prev, _mid, _next)
    }

    inline fun insert(prev: Int, some: Int, next: Int) {
        nexts[prev] = some
        prevs[some] = prev
        nexts[some] = next
        prevs[next] = some
    }

    // fun Int.next() = nexts[this]
    // fun Int.prev() = prevs[this]
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var st = StringTokenizer(br.readLine())

    val initStationSize = st.nextToken().toInt()
    val constructionSize = st.nextToken().toInt()

    st = StringTokenizer(br.readLine())
    val initStations = List(initStationSize) { st.nextToken().toInt() }

    val nexts = IntArray(1_000_001) { -1 }
    val prevs = IntArray(1_000_001) { -1 }

    (0 until initStationSize).forEach { i ->
        val _this = initStations[i]
        val _next = initStations[(i + 1) % initStationSize]
        val _prev = initStations[(i - 1 + initStationSize) % initStationSize]

        nexts[_this] = _next
        prevs[_this] = _prev
    }

    val stations = MapNodes(nexts = nexts, prevs = prevs)

    val bw = BufferedWriter(OutputStreamWriter(System.out))
    repeat(constructionSize) {
        st = StringTokenizer(br.readLine())
        val command = st.nextToken()
        when (command) {
            "BN" -> {
                val i = st.nextToken().toInt()
                val j = st.nextToken().toInt()

                bw.write("${nexts[i]}\n")
                stations.insertNext(i, j)
            }

            "BP" -> {
                val i = st.nextToken().toInt()
                val j = st.nextToken().toInt()

                bw.write("${prevs[i]}\n")
                stations.insertPrev(i, j)
            }

            "CN" -> {
                val i = st.nextToken().toInt()
                val n = nexts[i]!!

                bw.write("${n}\n")
                stations.pop(n)
            }

            "CP" -> {
                val i = st.nextToken().toInt()
                val p = prevs[i]!!

                bw.write("${p}\n")
                stations.pop(p)
            }
        }
    }

    bw.flush()
    bw.close()
    br.close()
}
