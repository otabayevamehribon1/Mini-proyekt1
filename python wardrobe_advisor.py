import tkinter as tk
from tkinter import ttk, messagebox

class SmartWardrobeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("👔 Smart Garderob Yordamchisi")
        self.root.geometry("680x660")
        self.root.configure(bg="#f0f2f5")
        self.root.resizable(False, False)

        # 2. MA'LUMOTLAR BAZASI
        self.clothing_db = {
            "office": {
                "male": {
                    "hot": ["Yengil ko'ylak", "Chino shim", "Loafer oyoq kiyim"],
                    "cold": ["Ko'ylak", "Pidjak", "Shim", "Palto", "Tufli"],
                    "rainy": ["Suv o'tkazmaydigan pidjak", "Shim", "Rezina etik"]
                },
                "female": {
                    "hot": ["Bluzka", "Yubka yoki engil shim", "Balyonka"],
                    "cold": ["Triko ko'ylak", "Jinsi", "Uzun palto", "Etik"],
                    "rainy": ["Waterproof kurtka", "Shim", "Suv o'tkazmaydigan poyabzal"]
                }
            },
            "wedding": {
                "male": {
                    "hot": ["Yengil kostyum", "Oq ko'ylak", "Galstuk", "Klassik tufli"],
                    "cold": ["To'q rangli kostyum", "Ko'ylak", "Galstuk", "Palto", "Tufli"],
                    "rainy": ["Kostyum", "Yomg'irga chidamli plash", "Tufli"]
                },
                "female": {
                    "hot": ["Yengil kokteyl ko'ylagi", "Baland poshnali tuflilar"],
                    "cold": ["Uzun kechki libos", "Mo'yna yoki jun shol", "Tuflilar"],
                    "rainy": ["Kechki libos", "Chiroyli plash", "Tuflilar"]
                }
            },
            "gym": {
                "male": {
                    "hot": ["Sport futbolkasi", "Shortik", "Krossovka"],
                    "cold": ["Uzun yengli sport ko'ylagi", "Jogging shim", "Krossovka"],
                    "rainy": ["Sport futbolkasi", "Shortik", "Yomg'ir kurtkasi", "Krossovka"]
                },
                "female": {
                    "hot": ["Sport topi", "Leggings", "Krossovka"],
                    "cold": ["Uzun yengli sport topi", "Leggings", "Krossovka"],
                    "rainy": ["Sport topi", "Leggings", "Yomg'ir kurtkasi", "Krossovka"]
                }
            },
            "casual": {
                "male": {
                    "hot": ["Futbolka", "Shortik", "Sandal yoki keds"],
                    "cold": ["Sviter", "Jinsi", "Kurtka", "Krossovka"],
                    "rainy": ["Hudi", "Jinsi", "Yomg'ir kurtkasi", "Krossovka"]
                },
                "female": {
                    "hot": ["Mayka", "Shortik yoki yengil ko'ylak", "Sandal"],
                    "cold": ["Jinsi", "Sviter", "Kurtka", "Botinka"],
                    "rainy": ["Jinsi", "Waterproof kurtka", "Krossovka"]
                }
            }
        }

        self._setup_ui()

    def _setup_ui(self):
        # Sarlavha paneli
        header = tk.Frame(self.root, bg="#1e3a8a", height=90)
        header.pack(fill="x")
        tk.Label(header, text="👗 Kiyim Tavsiya Tizimi", font=("Segoe UI", 22, "bold"), 
                 bg="#1e3a8a", fg="#ffffff").pack(pady=25)

        # Asosiy konteyner
        main = tk.Frame(self.root, bg="#f0f2f5")
        main.pack(fill="both", expand=True, padx=30, pady=20)

        # Kirish kartasi
        card = tk.Frame(main, bg="#ffffff", bd=1, relief="solid")
        card.pack(fill="x", pady=(0, 15))

        # Combobox yaratish yordamchi funksiyasi
        self.gender_cb = self._make_input_row(card, "👤 Jins:", ["Erkak", "Ayol"])
        self.dest_cb = self._make_input_row(card, "📍 Manzil:", ["Ofis", "To'y", "Sport zal", "Oddiy sayr"])
        self.weather_cb = self._make_input_row(card, "🌤 Ob-havo:", ["Issiq", "Sovuq", "Yomg'irli"])

        # Tugmalar
        btn_box = tk.Frame(main, bg="#f0f2f5")
        btn_box.pack(fill="x", pady=10)

        self.btn_rec = tk.Button(btn_box, text="✨ Tavsiya olish", bg="#3b82f6", fg="white",
                                 font=("Segoe UI", 12, "bold"), relief="flat", bd=0, height=2,
                                 cursor="hand2", command=self._show_result)
        self.btn_rec.pack(side="left", fill="both", expand=True, padx=(0, 5))
        self._hover_effect(self.btn_rec, "#2563eb", "#3b82f6")

        self.btn_clr = tk.Button(btn_box, text="🔄 Tozalash", bg="#ef4444", fg="white",
                                 font=("Segoe UI", 12, "bold"), relief="flat", bd=0, height=2,
                                 cursor="hand2", command=self._clear_all)
        self.btn_clr.pack(side="left", fill="both", expand=True, padx=(5, 0))
        self._hover_effect(self.btn_clr, "#dc2626", "#ef4444")

        # Natija kartasi
        tk.Label(main, text="📋 Tavsiya etilgan kiyimlar:", font=("Segoe UI", 13, "bold"), 
                 bg="#f0f2f5", fg="#1f2937").pack(anchor="w", pady=(10, 5))

        res_card = tk.Frame(main, bg="#ffffff", bd=1, relief="solid")
        res_card.pack(fill="both", expand=True)

        self.res_txt = tk.Text(res_card, font=("Segoe UI", 11), bg="#fafafa", fg="#374151",
                               relief="flat", bd=0, padx=15, pady=10, state="disabled", wrap="word")
        scr = ttk.Scrollbar(res_card, orient="vertical", command=self.res_txt.yview)
        self.res_txt.configure(yscrollcommand=scr.set)
        self.res_txt.pack(side="left", fill="both", expand=True)
        scr.pack(side="right", fill="y")

        # Boshlang'ich holat
        self._update_text("👉 Yuqoridagi maydonlarni tanlab, \"Tavsiya olish\" tugmasini bosing.", "#6b7280")

    def _make_input_row(self, parent, label_text, values):
        """Chiroyli Label + Combobox qatori"""
        row = tk.Frame(parent, bg="#ffffff")
        row.pack(fill="x", padx=20, pady=12)
        
        tk.Label(row, text=label_text, bg="#ffffff", fg="#374151", 
                 font=("Segoe UI", 11, "bold")).pack(side="left", padx=5)
        
        cb = ttk.Combobox(row, values=values, state="readonly", width=22, font=("Segoe UI", 11))
        cb.pack(side="right", padx=5, fill="x", expand=True)
        cb.current(0)  # Avtomatik birinchi qiymatni tanlaydi (bo'sh qolishini oldini oladi)
        return cb

    def _hover_effect(self, btn, hover_color, normal_color):
        """Tugma ustiga sichqoncha kelganda rang o'zgarishi"""
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=normal_color))

    def _show_result(self):
        """3. MANTIQ: Ma'lumotlarni olish va qayta ishlash"""
        gender = self.gender_cb.get()
        dest = self.dest_cb.get()
        weather = self.weather_cb.get()

        # Xavfsiz xaritlash
        maps = {
            "gender": {"Erkak": "male", "Ayol": "female"},
            "dest": {"Ofis": "office", "To'y": "wedding", "Sport zal": "gym", "Oddiy sayr": "casual"},
            "weather": {"Issiq": "hot", "Sovuq": "cold", "Yomg'irli": "rainy"}
        }

        try:
            g, d, w = maps["gender"][gender], maps["dest"][dest], maps["weather"][weather]
            outfit = self.clothing_db[d][g][w]
            
            msg = f"📍 {dest} ga borish uchun ({weather} ob-havo, {gender})\n\n"
            for item in outfit:
                msg += f"✅ {item}\n"
            self._update_text(msg, "#059669")
            
        except KeyError:
            messagebox.showerror("Xatolik", "Ma'lumotlar bazasida kutilmagan nom topildi.")
            self._update_text("❌ Xatolik yuz berdi. Qayta urinib ko'ring.", "#dc2626")

    def _update_text(self, text, color="#374151"):
        """Matn maydonini xavfsiz yangilash"""
        self.res_txt.config(state="normal")
        self.res_txt.delete("1.0", tk.END)
        self.res_txt.insert(tk.END, text)
        self.res_txt.tag_configure("c", foreground=color)
        self.res_txt.tag_add("c", "1.0", "end")
        self.res_txt.config(state="disabled")

    def _clear_all(self):
        self.gender_cb.current(0)
        self.dest_cb.current(0)
        self.weather_cb.current(0)
        self._update_text("👉 Maydonlar tozalandi. Yangi kombinatsiya tanlang.", "#6b7280")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartWardrobeApp(root)
    root.mainloop()





