def make_pg_url(
    host: str,
    port: int,
    username: str,
    password: str,
    db_name: str,
) -> str:
    return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"