import java.util.PriorityQueue
import kotlin.math.abs

object BJ11286 {
    fun solution(arr: List<Int>): List<Int> {
        data class Num(val num: Int) {
            val abs: Int = abs(num)
        }

        val pq: PriorityQueue<Num> = PriorityQueue(compareBy({ it.abs }, { it.num }))
        val answer = mutableListOf<Int>()
        arr.forEach {
            if (it == 0) {
                if (pq.isEmpty()) {
                    answer.add(0)
                } else {
                    answer.add(pq.poll().num)
                }
            } else {
                pq.add(Num(it))
            }
        }
        return answer
    }

    fun solve() {
        val br = System.`in`.bufferedReader()
        val n = br
                .readLine()
                .toInt()
        val arr = mutableListOf<Int>()
        repeat(n) {
            arr.add(
                br
                        .readLine()
                        .toInt()
            )
        }
        solution(arr).forEach { println(it) }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
