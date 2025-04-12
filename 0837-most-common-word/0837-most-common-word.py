class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:        
        paragraph = re.sub(r'[^a-zA-Z\s]', ' ', paragraph.lower())

        counter = defaultdict(int)
        for word in paragraph.split():
            if word not in banned:
                counter[word] += 1       

        return max(counter, key=counter.get)