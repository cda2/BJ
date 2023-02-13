object BJ1041 {

    fun solution(n: Long, dice: List<Int>): Long {
        val newDice = dice.map { it.toLong() }
        val minDiceSum = arrayListOf<Long>()
        val (a, b, c, d, e) = (0..4).map { newDice[it] }
        val f = newDice[5]
        minDiceSum.add(newDice.min())
        minDiceSum.add(
            minOf(
                a + b, a + c, a + d, a + e, b + c, b + d, b + f, c + e, c + f, d + e, d + f, e + f))
        minDiceSum.add(
            minOf(
                a + b + c,
                a + b + d,
                a + c + e,
                a + d + e,
                b + c + f,
                b + d + f,
                c + e + f,
                d + e + f))

        return when (n) {
            1L -> {
                newDice.sum() - newDice.max()
            }
            else -> {
                val (oneSum, twoSum, threeSum) = minDiceSum
                var answer = 4 * threeSum
                answer += (8 * n - 12) * twoSum
                answer += (5 * n * n - 16 * n + 12) * oneSum

                answer
            }
        }
    }

    fun solve() {
        val n = readln().toLong()
        val dice = readln().split(" ").map { it.toInt() }
        println(solution(n, dice))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
