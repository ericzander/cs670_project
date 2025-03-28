category_translation_map = {
    # English categories (unchanged)
    "Action": "Action",
    "Free To Play": "Free To Play",
    "Free to Play": "Free To Play",
    "Indie": "Indie",
    "Strategy": "Strategy",
    "RPG": "RPG",
    "Casual": "Casual",
    "Simulation": "Simulation",
    "Racing": "Racing",
    "Massively Multiplayer": "Massively Multiplayer",
    "Sports": "Sports",
    "Early Access": "Early Access",
    "Utilities": "Utilities",
    "Video Production": "Video Production",
    "Design & Illustration": "Design & Illustration",
    "Education": "Education",
    "Game Development": "Game Development",
    "Web Publishing": "Web Publishing",
    "Photo Editing": "Photo Editing",
    "Software Training": "Software Training",
    "Sexual Content": "Sexual Content",
    "Nudity": "Nudity",
    "Violent": "Violent",
    "Gore": "Gore",
    "Movie": "Movie",
    "Documentary": "Documentary",
    "Episodic": "Episodic",
    "Short": "Short",
    "Tutorial": "Tutorial",
    "Accounting": "Accounting",
    "Animation & Modeling": "Animation & Modeling",
    "Audio Production": "Audio Production",
    
    # Translations for non-English categories
    "Экшены": "Action",
    "Бесплатные": "Free To Play",
    "Стратегии": "Strategy",
    "Инди": "Indie",
    "Приключенческие игры": "Adventure",
    "Ролевые игры": "RPG",
    "Akcja": "Action",
    "Akční": "Action",
    "Dobrodružné": "Adventure",
    "动作": "Action",
    "独立": "Indie",
    "策略": "Strategy",
    "角色扮演": "RPG",
    "Acción": "Action",
    "Симуляторы": "Simulation",
    "Гонки": "Racing",
    "Спортивные игры": "Sports",
    "Aventura": "Adventure",
    "Многопользовательские игры": "Massively Multiplayer",
    "Indépendant": "Indie",
    "Stratégie": "Strategy",
    "Carreras": "Racing",
    "Deportes": "Sports",
    "Niezależne": "Indie",
    "Strategie": "Strategy",
    "模拟": "Simulation",
    "アクション": "Action",
    "アドベンチャー": "Adventure",
    "インディー": "Indie",
    "Simulationen": "Simulation",
    "Abenteuer": "Adventure",
    "Rollenspiel": "RPG",
    "冒険": "Adventure",
    "冒險": "Adventure",
    "冒险": "Adventure",
    "Eventyr": "Adventure",
    "Strategi": "Strategy",
    "Казуальные игры": "Casual",
    "Avventura": "Adventure",
    "Azione": "Action",
    "Actie": "Action",
    "Пригоди": "Adventure",
    "Estrategia": "Strategy",
    "Roolipelit": "RPG",
    "Seikkailu": "Adventure",
    "Strategia": "Strategy",
    "Ранний доступ": "Early Access",
    "Sport": "Sports",
    "Simulaatio": "Simulation",
    "ストラテジー": "Strategy",
    "Бойовики": "Action",
    "免费开玩": "Free To Play",
    "Інді": "Indie",
    "Казуальні ігри": "Casual",
    "Simuladores": "Simulation",
    "Free-to-play": "Free To Play",
    "Massivement multijoueur": "Massively Multiplayer",
    "動作": "Action",
    "大型多人連線": "Massively Multiplayer",
    "搶先體驗": "Early Access",
    "Acceso anticipado": "Early Access",
    "Utilidades": "Utilities",
    "Occasionnel": "Casual",
    "Kostenlos spielbar": "Free To Play",
    "MMO": "Massively Multiplayer",
    "Multijugador masivo": "Massively Multiplayer",
    "獨立製作": "Indie",
    "Avontuur": "Adventure",
    "Race": "Racing",
    "Simulatie": "Simulation",
    "休闲": "Casual",
    "体育": "Sports",
    "Gelegenheitsspiele": "Casual",
    "抢先体验": "Early Access",
    "カジュアル": "Casual",
    "無料プレイ": "Free To Play",
    "Simulering": "Simulation",
    "休閒": "Casual",
    "模擬": "Simulation",
    "GDR": "RPG",
    "Passatempo": "Casual",
    "Course automobile": "Racing",
    "Estratégia": "Strategy",
    "Grátis para Jogar": "Free To Play",
    "Simulação": "Simulation",
    "Ação": "Action",
    "Rol": "RPG",
    "Aventure": "Adventure",
}


import pandas as pd

if __name__ == "__main__":
    # Load the CSV file
    df = pd.read_csv("data/oct24_clean/genres.csv", encoding="utf-8")

    # Specify the column that needs translation
    column_name = "genre"

    # Apply translation using the dictionary
    df[column_name] = df[column_name].str.strip()
    df[column_name] = df[column_name].replace(category_translation_map)

    # Save the updated CSV
    df.to_csv("data/oct24_clean/genres_translated.csv", index=False)
