async function buscarOrdens() {
    const baseUrl = document.getElementById('baseUrl').value;
    const output = document.getElementById('output');
  
    output.textContent = "Carregando...";
  
    try {
      const res = await fetch(baseUrl + "/ordens");
  
      if (!res.ok) {
        throw new Error("Erro na requisição");
      }
  
      const data = await res.json();
  
      output.textContent = JSON.stringify(data, null, 2);
  
    } catch (err) {
      output.textContent = "Erro ao conectar com a API";
    }
  }