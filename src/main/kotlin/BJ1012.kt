object BJ1012 {
    data class Pos(val y: Int, val x: Int) {
        fun moveRight(): Pos = Pos(y, x + 1)
        fun moveLeft(): Pos = Pos(y, x - 1)
        fun moveUp(): Pos = Pos(y - 1, x)
        fun moveDown(): Pos = Pos(y + 1, x)
    }

    fun Array<BooleanArray>.isTrue(pos: Pos): Boolean = this[pos.y][pos.x]
    fun Array<BooleanArray>.visit(pos: Pos) {
        this[pos.y][pos.x] = true
    }
    fun Array<BooleanArray>.isValidPos(pos: Pos): Boolean =
        pos.y in indices && pos.x in 0 until this[0].size
    fun Array<BooleanArray>.getSize(): Pos = Pos(this.size, this[0].size)

    fun solution(m: Int, n: Int, cabbages: List<Pos>): Int {
        val cabbageStatus: Array<BooleanArray> = Array(m) { BooleanArray(n) { false } }
        for (cPos in cabbages) {
            cabbageStatus.visit(cPos)
        }

        val visitedStatus: Array<BooleanArray> = Array(m) { BooleanArray(n) { false } }
        var count = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                val pos = Pos(i, j)
                if (isNeedToVisit(cabbageStatus, visitedStatus, pos).not()) {
                    continue
                }

                dfs(cabbageStatus, visitedStatus, pos)
                count++
            }
        }

        return count
    }

    fun isNeedToVisit(
        cabbageStatus: Array<BooleanArray>,
        visitedStatus: Array<BooleanArray>,
        pos: Pos
    ): Boolean {
        return cabbageStatus.isValidPos(pos) &&
            !visitedStatus.isTrue(pos) &&
            cabbageStatus.isTrue(pos)
    }

    private fun dfs(
        cabbageStatus: Array<BooleanArray>,
        visitedStatus: Array<BooleanArray>,
        pos: Pos
    ) {
        if (isNeedToVisit(cabbageStatus, visitedStatus, pos).not()) {
            return
        }
        visitedStatus.visit(pos)
        dfs(cabbageStatus, visitedStatus, pos.moveRight())
        dfs(cabbageStatus, visitedStatus, pos.moveLeft())
        dfs(cabbageStatus, visitedStatus, pos.moveUp())
        dfs(cabbageStatus, visitedStatus, pos.moveDown())
    }

    fun solve() {
        val t = readln().toInt()
        repeat(t) {
            val (m, n, k) = readln().split(" ").map { it.toInt() }
            val cabbages = mutableListOf<Pos>()
            repeat(k) {
                val (x, y) = readln().split(" ").map { it.toInt() }
                cabbages.add(Pos(x, y))
            }
            println(solution(m, n, cabbages))
        }
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
