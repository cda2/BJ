import java.util.*

object BJ1697 {
    fun solution(from: Int, to: Int): Int {
        val dp = mutableMapOf<Int, Int>()

        data class State(val pos: Int, val count: Int) {
            fun nextStates(): List<State> {
                val nextStates = mutableListOf<State>()
                if (pos - 1 >= 0) nextStates.add(State(pos - 1, count + 1))
                if (pos + 1 <= 100000) nextStates.add(State(pos + 1, count + 1))
                if (pos * 2 <= 100000) nextStates.add(State(pos * 2, count + 1))
                return nextStates
            }

            fun isGoal(): Boolean = pos == to
            fun isVisited(): Boolean = dp.containsKey(pos)
        }

        fun bfs(state: State): Int {
            val queue = LinkedList<State>()
            queue.add(state)
            while (queue.isNotEmpty()) {
                val curState = queue.poll()
                if (curState.isGoal()) {
                    return curState.count
                }
                if (curState.isVisited()) continue
                dp[curState.pos] = curState.count
                for (nextState in curState.nextStates()) {
                    queue.add(nextState)
                }
            }
            return -1
        }

        return bfs(State(from, 0))
    }

    fun solve() {
        val (from, to) = readln()
                .split(" ")
                .map { it.toInt() }
        println(solution(from, to))
    }

    @JvmStatic
    fun main(args: Array<String>) {
        solve()
    }
}
