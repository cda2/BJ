object BJ7569 {
    enum class TomatoStatus(val status: Int) {
        NOT_EXIST(-1), NOT_RIPEN(0), RIPEN(1)
    }

    data class Pos(val y: Int, val z: Int, val x: Int) {
        private fun getAround(): Array<Pos> {
            return arrayOf(
                Pos(y - 1, z, x), Pos(y + 1, z, x), Pos(y, z - 1, x), Pos(y, z + 1, x),
                Pos(y, z, x - 1), Pos(y, z, x + 1)
            )
        }

        fun getNextPos(storage: Storage): List<Pos> {
            return getAround()
                    .filter { storage.isNotRipen(it) }
        }
    }

    class Storage(
        val tomatoes: Array<Array<IntArray>>,
    ) {
        val height = tomatoes.size
        val column = tomatoes[0].size
        val row = tomatoes[0][0].size
        private val visited: MutableMap<Pos, Boolean> =
            mutableMapOf<Pos, Boolean>().withDefault { false }

        private val ripenPosSet: MutableSet<Pos> = mutableSetOf()
        private var notRipenCount: Int = 0
        private var loopCount = 0

        init {
            for (y in 0 until height) {
                for (z in 0 until column) {
                    for (x in 0 until row) {
                        val pos = Pos(y, z, x)
                        when (getStatus(pos)) {
                            TomatoStatus.NOT_RIPEN -> notRipenCount++
                            TomatoStatus.RIPEN -> ripenPosSet.add(pos)
                            else -> Unit
                        }
                    }
                }
            }
        }

        fun getStatus(pos: Pos): TomatoStatus {
            return tomatoes[pos.y][pos.z][pos.x].let {
                when (it) {
                    -1 -> TomatoStatus.NOT_EXIST
                    0 -> TomatoStatus.NOT_RIPEN
                    1 -> TomatoStatus.RIPEN
                    else -> throw IllegalArgumentException("Invalid tomato status: $it")
                }
            }
        }

        fun isNotRipen(pos: Pos): Boolean {
            return isInStorage(pos) && getStatus(pos) == TomatoStatus.NOT_RIPEN
        }

        private fun isInStorage(pos: Pos): Boolean {
            return pos.y in 0 until height && pos.z in 0 until column && pos.x in 0 until row
        }

        fun changeRipen(pos: Pos) {
            if (this.isNotRipen(pos)) {
                this.tomatoes[pos.y][pos.z][pos.x] = TomatoStatus.RIPEN.status
                this.notRipenCount -= 1
            }
        }

        fun dayAfter() {
            for (pos in ripenPosSet.toSet()) {
                ripenPosSet.remove(pos)
                if (!visited.getValue(pos)) {
                    val nextPosList = pos.getNextPos(this)
                    for (nextPos in nextPosList) {
                        ripenPosSet.add(nextPos)
                        changeRipen(nextPos)
                    }
                }
                visited[pos] = true
            }

            loopCount++
        }

        fun countDaysUntilAllRipen(): Int {
            if (notRipenCount == 0) {
                return 0
            }

            while (true) {
                val beforeNotRipenCount: Int = this.notRipenCount
                dayAfter()
                val afterNotRipenCount: Int = this.notRipenCount

                if (beforeNotRipenCount == afterNotRipenCount) {
                    return if (notRipenCount != 0) {
                        -1
                    } else {
                        loopCount - 1
                    }
                }
            }
        }

    }

    fun solution(tomatoes: Array<Array<IntArray>>): Int {
        val storage = Storage(tomatoes)
        return storage.countDaysUntilAllRipen()
    }

    fun solve() {
        val bufferedReader = System.`in`.bufferedReader()
        val (m, n, h) = bufferedReader
                .readLine()
                .split(" ")
                .map { it.toInt() }
        val board = Array(h) { Array(n) { IntArray(m) } }
        repeat(h) { height ->
            repeat(n) { col ->
                val line = bufferedReader
                        .readLine()
                        .split(" ")
                        .map { it.toInt() }
                for ((row, value) in line.withIndex()) {
                    board[height][col][row] = value
                }
            }
        }
        println(solution(board))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
