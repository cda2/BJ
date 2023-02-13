object BJ11047 {
    fun solution(k: Int, coins: List<Int>): Int {
        var count = 0
        var remain = k
        for (coin in coins.sortedDescending()) {
            if (remain == 0) break
            if (coin > remain) continue
            count += remain / coin
            remain %= coin
        }
        return count
    }

    fun solve() {
        val bufferedReader = System.`in`.bufferedReader()
        val (n, k) = bufferedReader
                .readLine()
                .split(" ")
                .map { it.toInt() }
        val coins = mutableListOf<Int>()
        repeat(n) {
            coins.add(
                bufferedReader
                        .readLine()
                        .toInt()
            )
        }
        println(solution(k, coins))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
