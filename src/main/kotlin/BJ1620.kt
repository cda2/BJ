object BJ1620 {
    fun solution(arr: List<String>, queries: List<String>): List<String> {
        // create str to num, num to str map at once
        val strMap = mutableMapOf<String, Int>()
        val numMap = mutableMapOf<Int, String>()
        for (i in arr.indices) {
            strMap[arr[i]] = i
            numMap[i] = arr[i]
        }

        val answers = mutableListOf<String>()
        for (query in queries) {
            if (query[0].isDigit()) {
                answers.add(numMap[query.toInt() - 1]!!)
            } else {
                answers.add((strMap[query]!! + 1).toString())
            }
        }

        return answers
    }

    fun solve() {
        val (n, m) = readln()
                .split(" ")
                .map { it.toInt() }
        val arr = mutableListOf<String>()
        val queries = mutableListOf<String>()
        repeat(n) {
            arr.add(readln().trim())
        }
        repeat(m) {
            queries.add(readln().trim())
        }
        println(solution(arr, queries).joinToString("\n"))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
