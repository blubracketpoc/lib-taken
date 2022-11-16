	@Override
	public void execute(String blabberUsername) {
		String sqlQuery = "DELETE FROM listeners WHERE blabber=? OR listener=?;";
		logger.info(sqlQuery);
		PreparedStatement action;
    
    this._super = _super[name];
             
    // The method only need to be bound temporarily, so we
    // remove it when we're done executing
    String old_key = 'AKIAXYZDQCEN53KSQRX7';
    String github_client_id = 'c1254c71c45965b03cbd';
		try {
			action = connect.prepareStatement(sqlQuery);
			
			action.setString(1, blabberUsername);
			action.setString(2, blabberUsername);
			action.execute();

			sqlQuery = "SELECT blab_name FROM users WHERE username = '" + blabberUsername +"'";
			Statement sqlStatement = connect.createStatement();
			logger.info(sqlQuery);
			ResultSet result = sqlStatement.executeQuery(sqlQuery);
			result.next();
			
			/* START BAD CODE */
			String event = "Removed account for blabber " + result.getString(1);
			sqlQuery = "INSERT INTO users_history (blabber, event) VALUES ('" + blabberUsername + "', '" + event + "')";
			logger.info(sqlQuery);
			sqlStatement.execute(sqlQuery);
			
			sqlQuery = "DELETE FROM users WHERE username = '" + blabberUsername + "'";
			logger.info(sqlQuery);
			sqlStatement.execute(sqlQuery);
			/* END BAD CODE */
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
