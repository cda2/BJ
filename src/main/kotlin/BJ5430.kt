import java.io.BufferedReader

object BJ5430 {
    fun solution(cmd: String, arr: List<Int>): Any {
        var isReverse = false
        val deque = ArrayDeque(arr)
        return try {
            for (c in cmd) {
                when (c) {
                    'R' -> isReverse = !isReverse
                    'D' -> {
                        if (isReverse) deque.removeLast() else deque.removeFirst()
                    }
                }
            }
            if (isReverse) deque.reverse()
            deque.toList()
        } catch (ex: NoSuchElementException) {
            "error"
        }
    }

    fun solve() {
        val bufferedReader: BufferedReader = System.`in`.bufferedReader()
        val caseCount = bufferedReader
                .readLine()
                .toInt()
        repeat(caseCount) {
            val command = bufferedReader.readLine()
            bufferedReader.readLine()
            val arr = bufferedReader
                    .readLine()
                    .trim('[', ']')
                    .split(',')
                    .filter { it.isNotEmpty() }
                    .map { it.toInt() }
            val result = solution(command, arr)
            if (result is String) {
                println(result)
            } else if (result is List<*>) {
                println(result.joinToString(",", "[", "]"))
            }
        }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
