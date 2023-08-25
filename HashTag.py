class push_modal(ui.Modal, title="Push your code here"):
    language = ui.TextInput(label="Language", style=discord.TextStyle.short, default="py", required=True)
    problem = ui.TextInput(label="Problem", style=discord.TextStyle.short, required=True)
    code = ui.TextInput(label="Code", style=discord.TextStyle.paragraph,placeholder="Write your code here", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo("dmtrung14/leetcode_arxiv")
        filename=f'{self.problem}.{self.language}'
        message= f"Created solution for {self.problem}"
        content=f"{self.code}"