object BJ14500 {
    fun solution(paper: List<List<Int>>): Int {
        val visited: Array<BooleanArray> =
            Array(paper.size) { BooleanArray(paper[0].size) { false } }
        var maxValue: Int = Int.MIN_VALUE

        data class Pos(val y: Int, val x: Int) {
            private fun unvalidatedNextPos(): List<Pos> {
                return listOf(Pos(y, x + 1), Pos(y + 1, x), Pos(y, x - 1), Pos(y - 1, x))
            }

            fun isValid(): Boolean {
                return this.y in paper.indices && this.x in 0 until paper[0].size
            }

            fun isVisited(): Boolean {
                return visited[y][x]
            }

            fun visit() {
                visited[y][x] = true
            }

            fun unvisit() {
                visited[y][x] = false
            }

            fun nextPos(): List<Pos> {
                return unvalidatedNextPos()
                        .filter { it.isValid() }
                        .filter { !it.isVisited() }
            }

            fun getValue(): Int {
                return paper[y][x]
            }
        }


        fun dfs(pos: Pos, curSum: Int = 0, curVisitCount: Int = 1) {

            if (curVisitCount == 4) {
                maxValue = maxOf(maxValue, curSum)
                return
            }

            for (nextPos in pos.nextPos()) {
                if (curVisitCount == 2) {
                    nextPos.visit()
                    dfs(pos, curSum + nextPos.getValue(), curVisitCount + 1)
                    nextPos.unvisit()
                }
                nextPos.visit()
                dfs(nextPos, curSum + nextPos.getValue(), curVisitCount + 1)
                nextPos.unvisit()
            }
        }


        for (row in paper.indices) {
            for (col in paper[0].indices) {
                val pos = Pos(row, col)
                pos.visit()
                dfs(pos, pos.getValue())
                pos.unvisit()
            }
        }

        return maxValue
    }

    fun solve() {
        val bufferedReader = System.`in`.bufferedReader()
        val (n, m) = bufferedReader
                .readLine()
                .split(" ")
                .map { it.toInt() }
        val paper: MutableList<List<Int>> = mutableListOf()
        repeat(n) {
            paper.add(
                bufferedReader
                        .readLine()
                        .split(" ")
                        .map { it.toInt() }
                        .toList()
            )
        }
        println(solution(paper))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
