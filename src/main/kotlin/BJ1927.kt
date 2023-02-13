import java.util.PriorityQueue

object BJ1927 {
    fun solution(list: List<Long>): List<Long> {
        val priorityQueue = PriorityQueue<Long>()
        val answers = mutableListOf<Long>()
        for (value in list) {
            if (value == 0L) {
                answers.add(
                    when {
                        priorityQueue.isEmpty() -> 0L
                        else -> priorityQueue.poll()
                    }
                )
            } else {
                priorityQueue.add(value)
            }
        }
        return answers
    }

    fun solve() {
        val n = readln().toInt()
        val list = mutableListOf<Long>()
        repeat(n) {
            list.add(readln().toLong())
        }
        println(solution(list).joinToString("\n"))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
