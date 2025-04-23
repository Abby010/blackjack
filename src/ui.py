from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_title_screen():
    title_text = Text()
    title_text.append("\n♠️ ♣️ ♦️ ♥️  ", style="bold cyan")
    title_text.append("BLACKJACK\n", style="bold white on black")
    title_text.append("♠️ ♣️ ♦️ ♥️  \n", style="bold cyan")
    title_text.append("\n", style="bold")

    intro = Panel.fit(
        title_text,
        title="🎲 Welcome to the Table 🎲",
        border_style="bright_magenta",
    )

    console.print(intro)
