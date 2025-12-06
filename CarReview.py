from flask import Flask, render_template, jsonify, abort, request
import os, json, time

app = Flask(__name__)

# ===================== DADOS DAS MARCAS =====================
BRANDS = {
    "audi": {
        "nome": "Audi",
        "folder": "audi",
        "pais": "🇩🇪 Alemanha",
        "tagline": "Luxo esportivo alemão",
        "badge": "premium",
        "modelos": [
            {"nome": "A3", "nota": 4.6, "descricao": "Compacto premium equilibrado, muito popular no Brasil."},
            {"nome": "Q5", "nota": 4.7, "descricao": "SUV médio com bom acabamento e tecnologia."},
            {"nome": "RS5", "nota": 4.9, "descricao": "Coupé esportivo agressivo, foco total em performance."}
        ]
    },

    "bmw": {
        "nome": "BMW",
        "folder": "bmw",
        "pais": "🇩🇪 Alemanha",
        "tagline": "Dirigibilidade e desempenho",
        "badge": "sport",
        "modelos": [
            {"nome": "320i", "nota": 4.8, "descricao": "Sedã equilibrado, desempenho x conforto."},
            {"nome": "X1", "nota": 4.5, "descricao": "SUV compacto premium, urbano."},
            {"nome": "X6", "nota": 4.7, "descricao": "SUV cupê musculoso e chamativo."}
        ]
    },

    "chevrolet": {
        "nome": "Chevrolet",
        "folder": "chevrolet",
        "pais": "🇺🇸 EUA",
        "tagline": "Popular e acessível",
        "badge": "popular",
        "modelos": [
            {"nome": "Onix", "nota": 4.4, "descricao": "Hatch muito vendido, custo-benefício."},
            {"nome": "Tracker", "nota": 4.5, "descricao": "SUV compacto urbano, bem equipado."},
            {"nome": "S10", "nota": 4.3, "descricao": "Picape média tradicional, trabalho e estrada."}
        ]
    },

    "fiat": {
        "nome": "Fiat",
        "folder": "fiat",
        "pais": "🇮🇹 Itália",
        "tagline": "Cidade e economia",
        "badge": "cidade",
        "modelos": [
            {"nome": "Argo", "nota": 4.2, "descricao": "Hatch prático e barato de manter."},
            {"nome": "Cronos", "nota": 4.1, "descricao": "Sedã urbano, bom porta-malas."},
            {"nome": "Toro", "nota": 4.6, "descricao": "Picape média/monobloco, bem popular."}
        ]
    },

    "ford": {
        "nome": "Ford",
        "folder": "ford",
        "pais": "🇺🇸 EUA",
        "tagline": "Força e tradição pickup",
        "badge": "pickup",
        "modelos": [
            {"nome": "Ka", "nota": 3.9, "descricao": "Compacto urbano básico."},
            {"nome": "Ranger", "nota": 4.6, "descricao": "Picape média forte e tecnológica."},
            {"nome": "Mustang", "nota": 4.9, "descricao": "Ícone muscle car americano."}
        ]
    },

    "honda": {
        "nome": "Honda",
        "folder": "honda",
        "pais": "🇯🇵 Japão",
        "tagline": "Confiabilidade japonesa",
        "badge": "confiável",
        "modelos": [
            {"nome": "Civic", "nota": 4.8, "descricao": "Sedã médio clássico, bom equilíbrio geral."},
            {"nome": "HR-V", "nota": 4.6, "descricao": "SUV compacto confortável e bem construído."},
            {"nome": "Fit", "nota": 4.5, "descricao": "Hatch super prático e espaçoso."}
        ]
    },

    "hyundai": {
        "nome": "Hyundai",
        "folder": "hyundai",
        "pais": "🇰🇷 Coreia do Sul",
        "tagline": "Moderno e custo-benefício",
        "badge": "custo-benefício",
        "modelos": [
            {"nome": "HB20", "nota": 4.3, "descricao": "Hatch popular, atualizado sempre."},
            {"nome": "Creta", "nota": 4.4, "descricao": "SUV urbano cheio de versões."},
            {"nome": "Tucson", "nota": 4.2, "descricao": "SUV já tradicional da marca."}
        ]
    },

    "jeep": {
        "nome": "Jeep",
        "folder": "jeep",
        "pais": "🇺🇸 EUA",
        "tagline": "DNA off-road",
        "badge": "off-road",
        "modelos": [
            {"nome": "Renegade", "nota": 4.4, "descricao": "SUV compacto com visual Jeep mesmo nas versões básicas."},
            {"nome": "Compass", "nota": 4.5, "descricao": "SUV médio muito vendido no Brasil."},
            {"nome": "Wrangler", "nota": 4.9, "descricao": "Off-road raiz, ícone histórico da marca."}
        ]
    },

    "land_rover": {
        "nome": "Land Rover",
        "folder": "land_rover",
        "pais": "🇬🇧 Reino Unido",
        "tagline": "Luxo 4x4 britânico",
        "badge": "luxo 4x4",
        "modelos": [
            {"nome": "Evoque", "nota": 4.7, "descricao": "SUV premium compacto estiloso."},
            {"nome": "Discovery", "nota": 4.6, "descricao": "SUV familiar com foco em espaço e conforto."},
            {"nome": "Defender", "nota": 4.9, "descricao": "Off-road de luxo, releitura moderna de um clássico."}
        ]
    },

    "mercedes_benz": {
        "nome": "Mercedes Benz",
        "folder": "mercedes_benz",
        "pais": "🇩🇪 Alemanha",
        "tagline": "Executivo e conforto",
        "badge": "executivo",
        "modelos": [
            {"nome": "Classe A", "nota": 4.5, "descricao": "Compacto premium tecnológico."},
            {"nome": "GLA", "nota": 4.4, "descricao": "SUV compacto premium urbano."},
            {"nome": "GLE", "nota": 4.7, "descricao": "SUV maior, luxo e presença."}
        ]
    },

    "nissan": {
        "nome": "Nissan",
        "folder": "nissan",
        "pais": "🇯🇵 Japão",
        "tagline": "Tecnologia e eficiência",
        "badge": "tech",
        "modelos": [
            {"nome": "Kicks", "nota": 4.2, "descricao": "SUV compacto leve e econômico."},
            {"nome": "Sentra", "nota": 4.3, "descricao": "Sedã médio com pegada confortável."},
            {"nome": "Frontier", "nota": 4.4, "descricao": "Picape média robusta."}
        ]
    },

    "porsche": {
        "nome": "Porsche",
        "folder": "porsche",
        "pais": "🇩🇪 Alemanha",
        "tagline": "Performance e herança esportiva",
        "badge": "supercar",
        "modelos": [
            {"nome": "Macan", "nota": 4.8, "descricao": "SUV esportivo, Porsche de uso diário."},
            {"nome": "Cayenne", "nota": 4.7, "descricao": "SUV grande esportivo e de luxo."},
            {"nome": "911", "nota": 5.0, "descricao": "Esportivo lendário, referência mundial."}
        ]
    },

    "toyota": {
        "nome": "Toyota",
        "folder": "toyota",
        "pais": "🇯🇵 Japão",
        "tagline": "Durabilidade e valor de revenda",
        "badge": "durável",
        "modelos": [
            {"nome": "Corolla", "nota": 4.8, "descricao": "Sedã médio mais famoso do mundo."},
            {"nome": "Corolla Cross", "nota": 4.6, "descricao": "SUV derivado do Corolla, foco família."},
            {"nome": "Hilux", "nota": 4.9, "descricao": "Picape média super conhecida pela robustez."}
        ]
    },

    "volkswagen": {
        "nome": "Volkswagen",
        "folder": "volkswagen",
        "pais": "🇩🇪 Alemanha",
        "tagline": "Tradição alemã, apelo no Brasil",
        "badge": "alemã",
        "modelos": [
            {"nome": "Polo", "nota": 4.3, "descricao": "Hatch compacto esperto e popular."},
            {"nome": "T-Cross", "nota": 4.4, "descricao": "SUV compacto da VW, bem vendido."},
            {"nome": "Amarok", "nota": 4.6, "descricao": "Picape média com motor forte."}
        ]
    },

    # ============================
    # NOVAS MARCAS
    # ============================

    "mitsubishi": {
        "nome": "Mitsubishi",
        "folder": "mitsubishi",
        "pais": "🇯🇵 Japão",
        "tagline": "Tradição 4x4 japonesa e SUVs robustos",
        "badge": "4x4 japonês",
        "modelos": [
            {"nome": "Lancer", "nota": 4.3, "descricao": "Sedã esportivo conhecido no rally."},
            {"nome": "Triton", "nota": 4.4, "descricao": "Picape robusta 4x4 ideal para trabalho e aventura."},
            {"nome": "Pajero", "nota": 4.6, "descricao": "Ícone off-road feito para qualquer terreno."}
        ]
    },

    "citroen": {
        "nome": "Citroën",
        "folder": "citroen",
        "pais": "🇫🇷 França",
        "tagline": "Design único e conforto francês",
        "badge": "design francês",
        "modelos": [
            {"nome": "C3", "nota": 4.0, "descricao": "Hatch urbano econômico e alto."},
            {"nome": "DS4", "nota": 4.2, "descricao": "Hatch premium com foco em estilo."},
            {"nome": "C3 Picasso", "nota": 4.4, "descricao": "Minivan confortável e espaçosa."}
        ]
    },

    "peugeot": {
        "nome": "Peugeot",
        "folder": "peugeot",
        "pais": "🇫🇷 França",
        "tagline": "Design francês e boa dirigibilidade",
        "badge": "francesa",
        "modelos": [
            {"nome": "208", "nota": 4.1, "descricao": "Hatch moderno com painel i-Cockpit."},
            {"nome": "2008", "nota": 4.3, "descricao": "SUV compacto estiloso e bom de dirigir."},
            {"nome": "3008", "nota": 4.6, "descricao": "SUV médio muito premiado, interior de luxo."}
        ]
    },

    "jaguar": {
        "nome": "Jaguar",
        "folder": "jaguar",
        "pais": "🇬🇧 Reino Unido",
        "tagline": "Luxo britânico com esportividade",
        "badge": "luxo esportivo",
        "modelos": [
            {"nome": "XF", "nota": 4.5, "descricao": "Sedã executivo com muito luxo."},
            {"nome": "F-Pace", "nota": 4.6, "descricao": "SUV esportivo com elegância e tecnologia."},
            {"nome": "F-Type", "nota": 4.9, "descricao": "Esportivo icônico com desempenho máximo."}
        ]
    }
}

# ===================== HELPERS =====================

def _load_reviews():
    data_dir = os.path.join(app.root_path, "data")
    file_path = os.path.join(data_dir, "reviews.json")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except Exception:
                return []
    return []

# 🔥 NOVO: CÁLCULO GLOBAL DOS DESTAQUES
def compute_global_stats():
    reviews = _load_reviews()

    if not reviews:
        return {
            "global_avg": 0,
            "total_reviews": 0,
            "top_model": "---"
        }

    total_reviews = len(reviews)
    global_avg = round(sum(r["rating"] for r in reviews) / total_reviews, 1)

    # Modelo mais comentado
    model_counts = {}
    for r in reviews:
        key = f"{r['brand']} {r['model']}"
        model_counts[key] = model_counts.get(key, 0) + 1

    top_model = max(model_counts, key=model_counts.get)

    return {
        "global_avg": global_avg,
        "total_reviews": total_reviews,
        "top_model": top_model
    }

# ===================== ROTAS =====================

@app.route("/")
def index():
    return render_template("index.html")

# 🔥 NOVO: API PARA OS DESTAQUES
@app.route("/api/stats")
def api_stats():
    try:
        return jsonify({"success": True, **compute_global_stats()})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/marca/<nome_marca>")
def mostrar_marca(nome_marca):
    chave = nome_marca.replace("-", "_").lower()
    brand_data = BRANDS.get(chave)
    if not brand_data:
        return abort(404)

    brand = json.loads(json.dumps(brand_data))
    reviews = _load_reviews()
    folder = brand["folder"]

    for m in brand["modelos"]:
        matches = [
            r for r in reviews
            if r.get("brand") == folder and r.get("model") == m["nome"]
        ]
        if matches:
            m["nota"] = round(sum(r["rating"] for r in matches) / len(matches), 1)

    brand_matches = [r for r in reviews if r.get("brand") == folder]
    brand["qtd_avaliacoes"] = len(brand_matches)
    brand["media_comunidade"] = (
        round(sum(r["rating"] for r in brand_matches) / len(brand_matches), 1)
        if brand_matches else 0
    )

    return render_template("marca_base.html", brand=brand)

@app.route("/user_info")
def user_info():
    return jsonify({"message": "Autenticação via Firebase"})

@app.route("/api/review", methods=["GET", "POST"])
def api_review():
    try:
        data_dir = os.path.join(app.root_path, "data")
        os.makedirs(data_dir, exist_ok=True)
        file_path = os.path.join(data_dir, "reviews.json")

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    reviews = json.load(f)
                except Exception:
                    reviews = []
        else:
            reviews = []

        # ========== POST ==========
        if request.method == "POST":
            data = request.get_json(force=True)
            brand = data.get("brand")
            model = data.get("model")
            rating = int(data.get("rating", 0))

            if not brand or not model or rating < 1 or rating > 5:
                return jsonify({"success": False,"error": "Dados inválidos"}), 400

            new = {
                "brand": brand,
                "model": model,
                "rating": rating,
                "ts": int(time.time())
            }

            reviews.append(new)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(reviews, f, ensure_ascii=False, indent=2)

            matches = [r for r in reviews if r["brand"] == brand and r["model"] == model]
            avg = round(sum(r["rating"] for r in matches) / len(matches), 1)
            count = len(matches)

            brand_matches = [r for r in reviews if r["brand"] == brand]
            brand_avg = round(
                sum(r["rating"] for r in brand_matches) / len(brand_matches), 1
            )
            brand_count = len(brand_matches)

            # 🔥 AGORA DEVOLVE ESTATÍSTICAS GLOBAIS JUNTO
            stats = compute_global_stats()

            return jsonify({
                "success": True,
                "avg": avg,
                "count": count,
                "brand_avg": brand_avg,
                "brand_count": brand_count,
                "global_avg": stats["global_avg"],
                "total_reviews": stats["total_reviews"],
                "top_model": stats["top_model"]
            })

        # ========== GET ==========
        brand = request.args.get("brand")
        model = request.args.get("model")

        if not brand or not model:
            return jsonify({
                "success": False,
                "error": "Parâmetros brand/model obrigatórios"
            }), 400

        matches = [r for r in reviews if r["brand"] == brand and r["model"] == model]

        if not matches:
            return jsonify({"success": True, "count": 0, "avg": 0, "reviews": []})

        avg = round(sum(r["rating"] for r in matches) / len(matches), 1)
        matches_sorted = sorted(matches, key=lambda r: r["ts"], reverse=True)[:20]

        return jsonify({
            "success": True,
            "count": len(matches),
            "avg": avg,
            "reviews": matches_sorted
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ================================================================
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
# ================================================================
