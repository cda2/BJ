object BJ11403 {
    fun solution(graph: List<List<Int>>): List<List<Int>> {
        val size = graph.size
        val answer: List<MutableList<Int>> = graph.map { it.toMutableList() }

        for (mid in 0 until size) {
            for (start in 0 until size) {
                for (end in 0 until size) {
                    if (answer[start][mid].and(answer[mid][end]) == 1) {
                        answer[start][end] = 1
                    }
                }
            }
        }

        return answer
    }

    fun solve() {
        val bufferedReader = System.`in`.bufferedReader()
        val n = bufferedReader
                .readLine()
                .toInt()
        val graph = mutableListOf<List<Int>>()
        repeat(n) {
            graph.add(
                bufferedReader
                        .readLine()
                        .split(" ")
                        .map { it.toInt() }
                        .toList()
            )
        }
        solution(graph).forEach { println(it.joinToString(" ")) }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
