/**
 * {{SKILL_NAME}} - {{SKILL_DESCRIPTION}}
 * 
 * Usage:
 *   node script.js <param1> <param2>
 */

const fs = require('fs');
const path = require('path');

/**
 * メイン処理
 * @param {string} param1 - 入力パラメータ1
 * @param {string} param2 - 入力パラメータ2
 */
async function main(param1, param2) {
  try {
    console.log(`Processing with param1: ${param1}, param2: ${param2}`);
    
    // TODO: メイン処理を実装
    
    console.log('処理完了');
  } catch (error) {
    console.error('エラー:', error.message);
    process.exit(1);
  }
}

// CLI 引数から呼び出し
if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.log('Usage: node script.js <param1> <param2>');
    process.exit(1);
  }
  main(args[0], args[1]);
}

module.exports = { main };
