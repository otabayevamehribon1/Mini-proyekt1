import tkinter as tk
from tkinter import ttk, messagebox

# 1. MA'LUMOTLAR BAZASI (O'zbek milliy taomlari va retseptlari)
recipes_db = {
    "osh": """
    🍛 O'SH (PALOV) RETSEPTI
    
    Kerakli masalliqlar:
    - Guruch (Devzira yoki Lazat): 1 kg
    - Mol go'shti yoki qo'y go'shti: 500 gr
    - Sabzi (sariq va qizil): 1 kg
    - Piyoz: 3-4 dona
    - Sarimsoq: 2-3 bosh
    - Zig'ir yog'i yoki paxta yog'i: 150-200 ml
    - Zira, tuz, murch, zirk.

    Tayyorlanishi:
    1. Yog'ni qizdirib, piyozni qovurasiz.
    2. Go'shtni qo'shib, qizarasiz.
    3. To'g'ralgan sabzini qo'shib, yumshaguncha qovurasiz (Zirvak tayyorlash).
    4. Yuvgan guruchni tekis qilib solasiz.
    5. Ustiga suv quyib, dimlab pishirasiz.
    6. Oxirida sarimsoq va ziravorlarni qo'shasiz.
    """,

    "manti": """
    🥟 MANTI RETSEPTI
    
    Kerakli masalliqlar:
    - Un: 500 gr
    - Suv: 1 stakan
    - Tuxum: 1 dona
    - Qiyma (go'sht): 500 gr
    - Piyoz: 3-4 dona (mayda to'g'ralgan)
    - Qora murch, tuz.

    Tayyorlanishi:
    1. Xamirni qattiq qilib yoğrasiz va 30 daqiqa dam olasiz.
    2. Ichlik uchun go'sht va piyozni aralashtirasiz (piyoz ko'p bo'lishi kerak).
    3. Xamirdan kichik bo'laklar olib, yoyasiz.
    4. Ichlikni solib, mantiga shakl berasiz.
    5. Mantovarkada 40-45 daqiqa bug'da pishirasiz.
    6. Qatiq yoki smetana bilan dasturxonga tortasiz.
    """,

    "sho'rva": """
    🍲 SHO'RVA RETSEPTI
    
    Kerakli masalliqlar:
    - Go'sht (suyakli): 400 gr
    - Kartoshka: 3-4 dona
    - Sabzi: 1 dona
    - Pomidor: 2 dona
    - Bulg'or qalampiri: 1 dona
    - Reshon (yashil piyoz), ukrop.

    Tayyorlanishi:
    1. Go'shtni qaynatib, ko'pig'ini olasiz.
    2. To'g'ralgan kartoshka va sabzini solasiz.
    3. Qovurilgan pomidor va qalampirni qo'shasiz.
    4. Ziravorlar (zira, murch) sepasiz.
    5. Tayyor bo'lgach, maydalangan ko'katlar bilan bezaysiz.
    """,

    "lag'mon": """
    🍜 LAG'MON (UYG'URCHA) RETSEPTI
    
    Kerakli masalliqlar:
    - Un, tuz, suv (cho'ziladigan xamir uchun)
    - Go'sht: 300 gr
    - Sabzi, piyoz, bulg'or qalampiri, pomidor.
    - Sarimsoq, acchiq qalampir.

    Tayyorlanishi:
    1. Xamirni cho'zib, uzun ipchalarga aylantirasiz va qaynoq suvda pishirasiz.
    2. Alohida tovada go'sht va sabzavotlardan quyuq sous (varka) tayyorlaysiz.
    3. Lag'monni likopchaga solib, ustiga varka quyib berilasiz.
    """,

    "norin": """
    🍝 NORIN RETSEPTI
    
    Kerakli masalliqlar:
    - Ot go'shti yoki mol go'shti
    - Xamir (tuxumli)
    - Piyoz, qora murch.

    Tayyorlanishi:
    1. Go'shtni yaxshilab qaynatib olasz.
    2. Xamirni yupqa yoyib, to'g'nab qaynatasiz.
    3. Qaynatilgan go'shtni maydalab, xamir bilan aralashtirasiz.
    4. Qaynatma (bulyon) bilan birga issiq holatda dasturxonga tortasiz.
    """,
    
    "dimlama": """
    🥘 DIMLAMA RETSEPTI
    
    Kerakli masalliqlar:
    - Go'sht, kartoshka, sabzi, piyoz, karam, pomidor, baqlajon.
    
    Tayyorlanishi:
    1. Barcha masalliqlarni yirik to'g'rab, qozonga qavat-qavat qilasiz.
    2. En pastiga go'sht, ustidan sabzavotlar.
    3. Ozgina suv quyib, og'zini mahkam yopasiz.
    4. Sekin olovda 1.5 - 2 soat dimlaysiz.
    """
}

class UzbekFoodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("O'zbek Milliy Taomlari - Retseptlar")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # --- HEADER (Sarlavha qismi) ---
        header_frame = tk.Frame(root, bg="#2c3e50", height=80)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="🇺🇿 O'zbek Milliy Taomlari", 
            font=("Helvetica", 20, "bold"), 
            fg="white", 
            bg="#2c3e50"
        )
        title_label.pack(pady=20)

        # --- QIDIRUV QISMI ---
        search_frame = tk.Frame(root, bg="#f0f0f0")
        search_frame.pack(pady=15, fill="x", padx=20)

        tk.Label(search_frame, text="Taom nomini yozing:", font=("Arial", 12), bg="#f0f0f0").pack(side="left")
        
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=30, bd=2, relief="groove")
        self.search_entry.pack(side="left", padx=10)
        self.search_entry.bind("<KeyRelease>", self.search_recipe) # Yozish bilan qidiradi

        search_btn = tk.Button(search_frame, text="Qidirish", command=self.search_recipe, bg="#27ae60", fg="white", font=("Arial", 10, "bold"))
        search_btn.pack(side="left", padx=5)

        # --- NATIJA CHIQADIGAN JOY (Text widget) ---
        result_frame = tk.Frame(root, bg="white", bd=2, relief="sunken")
        result_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Scrollbar qo'shamiz
        scrollbar = tk.Scrollbar(result_frame)
        scrollbar.pack(side="right", fill="y")

        self.result_text = tk.Text(
            result_frame, 
            font=("Courier New", 12), 
            wrap="word", 
            yscrollcommand=scrollbar.set,
            bg="#fff",
            fg="#333",
            padx=10,
            pady=10,
            state="disabled" # Dastlab bo'sh turishi uchun
        )
        self.result_text.pack(fill="both", expand=True)
        scrollbar.config(command=self.result_text.yview)

        # Dastlabki ko'rsatma
        self.show_message("Ro'yxatdan taom nomini tanlang yoki qidiruvga yozing.\n\nMasalan: Osh, Manti, Sho'rva...")

    def search_recipe(self, event=None):
        query = self.search_entry.get().lower().strip()
        
        if not query:
            self.show_message("Iltimos, taom nomini yozing...")
            return

        # Bazadan qidirish
        found_recipes = []
        for name, recipe in recipes_db.items():
            if query in name:
                found_recipes.append((name, recipe))

        if found_recipes:
            # Agar topilsa, birinchisini ko'rsatamiz (yoki hammasini ro'yxat qilish mumkin)
            # Hozircha eng mos kelganini chiqaramiz
            name, recipe = found_recipes[0]
            self.show_message(recipe)
        else:
            self.show_message(f"Kechirasiz, '{query}' bo'yicha hech qanday retsept topilmadi.\nBoshqa taom nomini urinib ko'ring.")

    def show_message(self, message):
        self.result_text.config(state="normal") # Yozish uchun ochamiz
        self.result_text.delete(1.0, tk.END)    # Eskisini o'chiramiz
        self.result_text.insert(tk.END, message)
        self.result_text.config(state="disabled") # O'qish uchun qulay bo'lsin deb yopamiz

if __name__ == "__main__":
    root = tk.Tk()
    app = UzbekFoodApp(root)
    root.mainloop()