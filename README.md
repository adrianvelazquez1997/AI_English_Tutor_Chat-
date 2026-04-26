# 🧠 AI English Tutor - Marianne_V2

Aplicación de Inteligencia Artificial para aprender inglés mediante un tutor conversacional multimodal basado en LLMs, RAG, voz e imagen.

El sistema integra una tutora virtual llamada **Marianne_V2**, capaz de corregir errores, explicar conceptos, mantener conversaciones naturales, generar voz y crear imágenes educativas manteniendo una identidad visual consistente.

## 🎯 Objetivo

Construir un **asistente inteligente de aprendizaje de inglés** con arquitectura modular, capaz de combinar:

- recuperación de conocimiento mediante RAG
- generación de respuestas estructuradas con LLMs
- voz mediante Text-to-Speech
- generación de imágenes educativas
- visualización del espacio vectorial de embeddings

---

## 🧩 Funcionalidades actuales

- 💬 Chat conversacional en inglés  
- ✏️ Corrección automática de frases  
- 📖 Explicación de errores gramaticales
- 📚 RAG con PDFs y DOCX usando FAISS
- 🔎 Recuperación de contexto relevante mediante embeddings
- 🔊 Text-to-Speech con OpenAI
- 🖼️ Generación de imágenes educativas con referencia visual de Marianne_V2 
- 🤖 Identidad visual del personaje mediante imágenes de referencia
- 📊 Visualización 3D del espacio vectorial con PCA + Plotly
- 🖥️ Interfaz interactiva con Gradio 

---

## 🏗️ Arquitectura

![System Flow](diagram.png)

El sistema sigue una arquitectura **RAG + LLM + Multimodal Output**, diseñada para simular un tutor de inglés inteligente.

### 🔄 Flujo del sistema

1. **Data Ingestion**
   - PDFs / DOCX → limpieza → chunking  
   - Embeddings (`text-embedding-3-small`)  
   - Almacenamiento en FAISS  

2. **Retrieval (RAG)**
   - Búsqueda semántica  
   - Selección de *Top-K chunks* relevantes  

3. **LLM**
   - Prompt = user + contexto + system prompt  
   - Modelo: `gpt-4o-mini`  
   - Salida estructurada (JSON)

4. **Decision Engine**
   - Parseo de respuesta  
   - Decide: texto / audio / imagen  

5. **Multimodal Output**
   - 🔊 TTS (audio)  
   - 🖼️ generación de imágenes  
   - 💬 respuesta textual  

6. **UI (Gradio)**
   - Chat interactivo  
   - Audio player  
   - Panel de imágenes  

7. **Embedding Visualization**
   - PCA + Plotly  
   - Visualización 3D del espacio vectorial  
