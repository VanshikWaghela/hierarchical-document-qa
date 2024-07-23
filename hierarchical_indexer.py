from dataclasses import dataclass
from typing import List, Any
import networkx as nx

@dataclass
class TreeNode:
    id: str
    content: str
    parent: Any = None
    children: List[Any] = None

    def __post_init__(self):
        if self.children is None:
            self.children = []

class HierarchicalIndexer:
    def __init__(self):
        self.tree = nx.DiGraph()

    def build_index(self, pages: List[dict]) -> nx.DiGraph:
        root = TreeNode(id="root", content="Textbook")
        self.tree.add_node(root.id, data=root)

        current_chapter = None
        current_section = None

        for i, page in enumerate(pages):
            content = page.page_content
            lines = content.split('\n')

            for line in lines:
                if line.strip().lower().startswith('chapter'):
                    chapter_node = TreeNode(id=f"chapter_{i}", content=line, parent=root)
                    self.tree.add_node(chapter_node.id, data=chapter_node)
                    self.tree.add_edge(root.id, chapter_node.id)
                    current_chapter = chapter_node
                    current_section = None
                elif line.strip() and current_chapter:
                    if current_section is None:
                        section_node = TreeNode(id=f"section_{i}", content=line, parent=current_chapter)
                        self.tree.add_node(section_node.id, data=section_node)
                        self.tree.add_edge(current_chapter.id, section_node.id)
                        current_section = section_node
                    else:
                        leaf_node = TreeNode(id=f"leaf_{i}", content=line, parent=current_section)
                        self.tree.add_node(leaf_node.id, data=leaf_node)
                        self.tree.add_edge(current_section.id, leaf_node.id)

        return self.tree