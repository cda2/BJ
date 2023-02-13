object BJ11724 {
    fun solution(nodeCount: Int, arr: List<Pair<Int, Int>>): Int {
        val graph = mutableMapOf<Int, MutableSet<Int>>()
        for (i in 1..nodeCount) {
            graph[i] = mutableSetOf()
        }
        for ((start, end) in arr) {
            graph[start]?.add(end)
            graph[end]?.add(start)
        }

        val visited = mutableSetOf<Int>()
        var count = 0
        for (key in graph.keys) {
            if (visited.contains(key)) {
                continue
            }
            count++
            val curSet = mutableSetOf<Int>()
            curSet.add(key)
            while (curSet.isNotEmpty()) {
                val cur = curSet.first()
                curSet.remove(cur)
                visited.add(cur)
                for (next in graph[cur]!!) {
                    if (!visited.contains(next)) {
                        curSet.add(next)
                    }
                }
            }
        }

        return if (count == 0) nodeCount else count
    }

    fun solve() {
        val (n, m) = readLineToIntList()
        val arr = mutableListOf<Pair<Int, Int>>()
        repeat(m) {
            val (a, b) = readLineToIntList()
            arr.add(Pair(a, b))
        }
        println(solution(n, arr))
    }

    private fun readLineToIntList() = readln()
            .split(" ")
            .map { it.toInt() }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
