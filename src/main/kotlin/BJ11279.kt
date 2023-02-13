import java.util.PriorityQueue

object BJ11279 {
    fun solution(list: List<Long>): List<Long> {
        // max heap
        val priorityQueue = PriorityQueue<Long>(reverseOrder())

        val answers = mutableListOf<Long>()
        for (value in list) {
            if (value == 0L) {
                answers.add(
                    when {
                        priorityQueue.isEmpty() -> 0L
                        else -> priorityQueue.remove()
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
