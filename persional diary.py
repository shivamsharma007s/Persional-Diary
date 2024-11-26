import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

class PersonalDiary:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Diary")
        self.root.geometry("500x500")
        
        # Title Label
        self.title_label = tk.Label(root, text="Personal Diary", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        # Text Box for Diary Entry
        self.text_box = tk.Text(root, wrap="word", font=("Helvetica", 12), height=15)
        self.text_box.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Save Button
        self.save_button = tk.Button(root, text="Save Entry", command=self.save_entry, font=("Helvetica", 12))
        self.save_button.pack(pady=5)
        
        # View Entries Button
        self.view_button = tk.Button(root, text="View Entries", command=self.view_entries, font=("Helvetica", 12))
        self.view_button.pack(pady=5)

    def save_entry(self):
        """Save the current diary entry to a file."""
        text = self.text_box.get("1.0", tk.END).strip()
        if text == "":
            messagebox.showwarning("Warning", "Diary entry is empty!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            with open(filename, "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"--- {timestamp} ---\n")
                file.write(text + "\n\n")
            self.text_box.delete("1.0", tk.END)
            messagebox.showinfo("Success", "Diary entry saved!")

    def view_entries(self):
        """View previously saved diary entries."""
        filename = filedialog.askopenfilename(
            defaultextension=".txt", 
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            try:
                with open(filename, "r") as file:
                    content = file.read()
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert("1.0", content)
            except Exception as e:
                messagebox.showerror("Error", f"Unable to open file: {e}")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalDiary(root)
    root.mainloop()


