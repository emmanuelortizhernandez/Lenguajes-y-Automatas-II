import { pool } from 'config/db';

export async function getUserInfo(email){
    var query = "SELECT us.id, us.name, us.email "+
                "FROM user us "+
                "WHERE us.email = "+email+" ;";
    try{
        let [result] = await pool.query(query);
        return result;
    }catch (error) {
      return false;  
  }
    
}
