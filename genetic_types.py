from typing import TypeAlias


Score: TypeAlias = float
Item: TypeAlias = int
Genes: TypeAlias = list[bool]

class Solution:
    genes: Genes = []
    score: Score = 0.0

    def __init__(self, genes : Genes, score : Score = 0.0):
        self.genes = genes
        self.score = score

    def __str__(self):
        formatted_genes = ""
        for gene in self.genes:
            formatted_genes += str(int(gene))
        return f"Solution(score={float(self.score):.3f}, genes={formatted_genes})"

    def __copy__(self):
        return type(self)(self.genes.copy(), self.score)
