class BJ14002 {
    fun solution(arr: IntArray): List<Int> {
        val dp = IntArray(arr.size) { 0 }
        val table = mutableListOf(0)
        var maxSize = 0

        for ((i, num) in arr.withIndex()) {
            table
                .binarySearch(num)
                .let { if (it < 0) it.inv() else it }
                .let {
                    dp[i] = it
                    if (it >= table.size) {
                        table.add(num)
                        maxSize = maxOf(maxSize, it + 1)
                    } else if (table[it] > num) {
                        table[it] = num
                    }
                }
        }

        val result = mutableListOf<Int>()
        for (i in dp.lastIndex downTo 0) {
            if (dp[i] == maxSize - 1) {
                result.add(arr[i])
                maxSize--
            }
        }

        return result.reversed()
    }

    fun solve() {
        val n = readln().toInt()
        val arr = readln().split(" ").map { it.toInt() }.toIntArray()
        println(solution(arr).size)
        println(solution(arr).joinToString(" "))
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            BJ14002().solve()
        }
    }
}
