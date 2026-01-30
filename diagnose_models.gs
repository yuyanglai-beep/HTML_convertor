/**
 * Gemini API 模型診斷工具
 * 用途：列出您的 API Key 實際可以使用的所有模型
 */

function diagnoseAvailableModels() {
  // 📍 請在此填入您的 API Key
  const API_KEY = "AIzaSyBph8Jma6wXrMj6kRGvimHrqpM4T4k3iQs";
  
  if (!API_KEY || API_KEY.includes("YOUR")) {
    Logger.log("❌ 請先填入您的 API Key");
    return;
  }
  
  Logger.log("🔍 開始檢測可用模型...\n");
  
  // 測試 ListModels API
  const listUrl = "https://generativelanguage.googleapis.com/v1beta/models?key=" + API_KEY;
  
  try {
    const response = UrlFetchApp.fetch(listUrl, {muteHttpExceptions: true});
    const code = response.getResponseCode();
    const text = response.getContentText();
    
    if (code !== 200) {
      Logger.log(`❌ API 錯誤 [${code}]:`);
      Logger.log(text);
      Logger.log("\n💡 建議：");
      Logger.log("1. 確認您的 API Key 是從 https://aistudio.google.com/apikey 取得");
      Logger.log("2. 確認 API Key 沒有過期");
      return;
    }
    
    const json = JSON.parse(text);
    
    if (!json.models || json.models.length === 0) {
      Logger.log("❌ 找不到任何可用模型");
      return;
    }
    
    Logger.log("✅ 找到 " + json.models.length + " 個可用模型：\n");
    Logger.log("=" .repeat(80));
    
    // 篩選支援 generateContent 的模型
    const supportedModels = json.models.filter(m => 
      m.supportedGenerationMethods && 
      m.supportedGenerationMethods.includes("generateContent")
    );
    
    Logger.log("\n📋 支援 generateContent 的模型 (" + supportedModels.length + " 個)：\n");
    
    supportedModels.forEach((model, i) => {
      Logger.log(`${i+1}. ${model.name}`);
      Logger.log(`   顯示名稱: ${model.displayName || 'N/A'}`);
      Logger.log(`   支援方法: ${model.supportedGenerationMethods.join(', ')}`);
      if (model.description) {
        Logger.log(`   說明: ${model.description.substring(0, 100)}...`);
      }
      Logger.log("");
    });
    
    Logger.log("=" .repeat(80));
    Logger.log("\n💡 建議使用的模型名稱（請複製到主程式）：");
    
    if (supportedModels.length > 0) {
      // 找出最新的模型
      const recommended = supportedModels.find(m => 
        m.name.includes("gemini-2") || 
        m.name.includes("flash") ||
        m.name.includes("pro")
      ) || supportedModels[0];
      
      Logger.log(`\n   ${recommended.name}\n`);
      Logger.log("使用範例：");
      Logger.log(`const url = "https://generativelanguage.googleapis.com/v1beta/${recommended.name}:generateContent?key=" + key;`);
    }
    
  } catch (e) {
    Logger.log("🔥 執行錯誤: " + e.message);
    Logger.log(e.stack);
  }
}
