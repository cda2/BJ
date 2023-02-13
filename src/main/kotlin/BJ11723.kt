object BJ11723 {
    class CommandExecutor {
        private val checkArr = BooleanArray(21) { false }

        fun execute(line: String): Any {
            val split = line.split(" ")
            val command = split[0]
            val num = if (split.size == 2) split[1].toInt() else 0

            return when (command) {
                "add" -> add(num)
                "remove" -> remove(num)
                "check" -> check(num)
                "toggle" -> toggle(num)
                "all" -> all()
                "empty" -> empty()
                else -> throw IllegalArgumentException("Invalid command")
            }
        }

        private fun add(num: Int) {
            checkArr[num] = true
        }

        private fun remove(num: Int) {
            checkArr[num] = false
        }

        private fun check(num: Int): Int {
            return if (checkArr[num]) 1 else 0
        }

        private fun toggle(num: Int) {
            checkArr[num] = !checkArr[num]
        }

        private fun all() {
            for (i in 1..20) {
                checkArr[i] = true
            }
        }

        private fun empty() {
            for (i in 1..20) {
                checkArr[i] = false
            }
        }
    }


    fun solve() {
        val bufferedReader = System.`in`.bufferedReader()
        val bufferedWriter = System.out.bufferedWriter()
        val n = bufferedReader
                .readLine()
                .toInt()
        val commandExecutor = CommandExecutor()
        repeat(n) {
            val line = bufferedReader.readLine()
            val result = commandExecutor.execute(line)
            if (result is Int) {
                bufferedWriter.write("$result\n")
            }
        }
        bufferedWriter.flush()
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
