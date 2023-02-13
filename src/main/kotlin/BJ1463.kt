import java.util.PriorityQueue

object BJ1463 {
    data class Cal(val num: Int, val count: Int) {
        fun divideBy3(): Cal = Cal(num / 3, count + 1)
        fun divideBy2(): Cal = Cal(num / 2, count + 1)
        fun minusOne(): Cal = Cal(num - 1, count + 1)
        fun isKeep(dp: IntArray): Boolean = dp[num] > count && num > 0
        fun nextCalList(): List<Cal> {
            val nextCals = arrayListOf<Cal>()
            if (num % 3 == 0) nextCals.add(divideBy3())
            if (num % 2 == 0) nextCals.add(divideBy2())
            if (num > 1) nextCals.add(minusOne())
            return nextCals
        }
    }
    fun IntArray.minDpUpdate(cal: Cal) {
        this[cal.num] = cal.count
    }
    fun solution(n: Int): Int {
        val queue: PriorityQueue<Cal> = PriorityQueue(compareBy { it.count })
        val dp = IntArray(n + 1) { Int.MAX_VALUE }
        queue.add(Cal(n, 0))
        dp[n] = 0

        while (queue.isNotEmpty()) {
            val cal = queue.poll()
            if (cal.num == 1) return cal.count
            if (cal.isKeep(dp)) continue
            val cals = cal.nextCalList()
            for (c in cals) {
                if (c.isKeep(dp)) {
                    dp.minDpUpdate(c)
                    queue.add(c)
                }
            }
        }

        return n - 1
    }

    fun solve() {
        val n = readln().toInt()
        println(solution(n))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
