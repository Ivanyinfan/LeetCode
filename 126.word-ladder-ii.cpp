/*
 * @lc app=leetcode id=126 lang=cpp
 *
 * [126] Word Ladder II
 */

// @lc code=start
class Solution {
public:
    unordered_map<string, vector<string>> adjList;
    vector<string> currPath;
    vector<vector<string>> shortestPaths;
    
    vector<string> findNeighbors(string &word, unordered_set<string>& wordList) {
        vector<string> neighbors;
        
        for (int i = 0; i < word.size(); i++) {
            char oldChar = word[i];   
            
            // replace the i-th character with all letters from a to z except the original character
            for (char c = 'a'; c <= 'z'; c++) {
                word[i] = c;
                
                // skip if the character is same as original or if the word is not present in the wordList
                if (c == oldChar || !wordList.count(word)) {
                    continue;
                }
                neighbors.push_back(word);
            }
            word[i] = oldChar;
        }
        return neighbors;
    }
    
    void backtrack(string &source, string &destination) {
        // store the path if we reached the endWord
        if (source == destination) {
            shortestPaths.push_back(currPath);
        }
        for (int i = 0; i < adjList[source].size(); i++) {
            currPath.push_back(adjList[source][i]);
            backtrack(adjList[source][i], destination);
            currPath.pop_back();
        }
    }
    
    void bfs(string beginWord, string endWord, unordered_set<string> wordList) {
        queue<string> q;
        q.push(beginWord);
        
        // remove the root word which is the first layer
        if (wordList.find(beginWord) != wordList.end()) {
            wordList.erase(wordList.find(beginWord));
        }
        
        unordered_map<string, int> isEnqueued;
        isEnqueued[beginWord] = 1;
        
        while (!q.empty())  {
            // visited will store the words of current layer
            vector<string> visited;
            
            for (int i = q.size() - 1; i >= 0; i--) {
                string currWord = q.front(); 
                q.pop();

                // findNeighbors will have the adjacent words of the currWord
                vector<string> neighbors = findNeighbors(currWord, wordList);
                for (auto word : neighbors) {
                    visited.push_back(word);
                    // add the edge from currWord to word in the list
                    adjList[currWord].push_back(word);
                    
                    if (isEnqueued.find(word) == isEnqueued.end()) {
                        q.push(word);
                        isEnqueued[word] = 1;
                    }
                }
            }
            // removing the words of the previous layer
            for (int i = 0; i < visited.size(); i++) {
                if (wordList.find(visited[i]) != wordList.end()) {
                    wordList.erase(wordList.find(visited[i]));
                }
            }
        }
    }
    
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        // copying the words into the set for efficient deletion in BFS
        unordered_set<string> copiedWordList(wordList.begin(), wordList.end());
        // build the DAG using BFS
        bfs(beginWord, endWord, copiedWordList);
        
        // every path will start from the beginWord
        currPath = {beginWord};
        // traverse the DAG to find all the paths between beginWord and endWord
        backtrack(beginWord, endWord);
        
        return shortestPaths;
    }
};

class Solution {
public:
    unordered_map<string, vector<string>> adjList;
    vector<string> currPath;
    vector<vector<string>> shortestPaths;
    
    vector<string> findNeighbors(string &word, unordered_set<string>& wordList) {
        vector<string> neighbors;
        
        for (int i = 0; i < word.size(); i++) {
            char oldChar = word[i];   
            
            // replace the i-th character with all letters from a to z except the original character
            for (char c = 'a'; c <= 'z'; c++) {
                word[i] = c;
                
                // skip if the character is same as original or if the word is not present in the wordList
                if (c == oldChar || !wordList.count(word)) {
                    continue;
                }
                neighbors.push_back(word);
            }
            word[i] = oldChar;
        }
        return neighbors;
    }
    
    void backtrack(string &source, string &destination) {
        // store the path if we reached the endWord
        if (source == destination) {
            shortestPaths.push_back(currPath);
        }
        for (int i = 0; i < adjList[source].size(); i++) {
            currPath.push_back(adjList[source][i]);
            backtrack(adjList[source][i], destination);
            currPath.pop_back();
        }
    }
    
    void addEdge(string &word1, string &word2, int direction) {
        if(direction == 1) {
            adjList[word1].push_back(word2);
        } else {
            adjList[word2].push_back(word1);
        }
    }
    
    bool bfs(string beginWord, string endWord, unordered_set<string> wordList) {
        if (wordList.count(endWord) == 0) {
            return false;
        }
        
        // remove the root word which is the first layer
        if (wordList.find(beginWord) != wordList.end()) {
            wordList.erase(wordList.find(beginWord));
        }

        unordered_set<string> forwardQueue, backwardQueue;
        forwardQueue.insert(beginWord);
        backwardQueue.insert(endWord);
        
        bool found = false;
        int direction = 1;
        
        while (forwardQueue.size() != 0)  {
            // visited will store the words of current layer
            unordered_set<string> visited;
            
            // swap the queues because we are always extending the forwardQueue
            if (forwardQueue.size() > backwardQueue.size()) {
                swap(forwardQueue, backwardQueue);
                direction ^= 1;
            }
            
            for (auto currWord : forwardQueue) {
                vector<string> neighbors = findNeighbors(currWord, wordList);

                 for (auto word : neighbors) {
                    
                     // if the backwardQueue already contains it we can stop after completing this level
                     if (backwardQueue.find(word) != backwardQueue.end()) {
                         found = true;
                         addEdge(currWord, word, direction);
                    
                     /* the word shouldn't be presnt in forwardQueue because if it is then the edge will
                        be between two words at the same level which we don't want */
                     } else if (!found && wordList.count(word) != 0 && forwardQueue.count(word) == 0) {
                         visited.insert(word);
                         addEdge(currWord, word, direction);
                     }
                 }
            }
            
            // removing the words of the previous layer
            for (auto currWord : forwardQueue) {
                if (wordList.find(currWord) != wordList.end()) {
                    wordList.erase(wordList.find(currWord));
                }
            }
            if (found) {
                break;
            }
            
            forwardQueue = visited;
        }
        return found;
    }
    
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        // copying the words into the set for efficient deletion in BFS
        unordered_set<string> copiedWordList(wordList.begin(), wordList.end());
        // build the DAG using BFS
        bool sequence_found = bfs(beginWord, endWord, copiedWordList);
        
        // There is no valid sequence that connects `beginWord` to `endWord`
        if (sequence_found == false) {
            return shortestPaths;
        }
        // every path will start from the beginWord
        currPath = {beginWord};
        // traverse the DAG to find all the paths between beginWord and endWord
        backtrack(beginWord, endWord);
        
        return shortestPaths;
    }
};
// @lc code=end

