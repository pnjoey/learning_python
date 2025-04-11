import pandas as pd
import json


# Excel to Dataframe
# with open('Mapping_new.xlsx', 'r'):
#     df = pd.read_excel('Mapping_new.xlsx',sheet_name='BCTC CTCP full')
#
#     df = df.drop('Số thứ tự',axis=1)
#
#     df = df.drop('Độ dài chuỗi',axis=1)
#     df = df.dropna(axis=0)
#
#     df = df.set_index('DB field (snake_case)')['Excel field'].to_dict()
# print(df)

# Write to json file
# with open('chung_khoan_new.json', 'w', encoding='utf-8') as f:
#     json.dump(df, f, ensure_ascii=False, indent=4)

filename = 'cstc_nh'
if 'bh' in filename:
    table_name = 'fs_insurance'
elif 'nh' in filename:
    table_name = 'fs_bank'
elif 'ctcp' in filename:
    table_name = 'fs_corporation'
else:
    table_name = 'fs_securities'

# Read json file
with open(f'{filename}.json','r') as f:
    data = json.load(f)
keys = list(data.keys())

# Convert to Model
# with open(f'{filename}_model.json','w') as file:
#     if filename.startswith('tmbctc'):
#         for line in keys:
#             file.write(f"{line}: Mapped[Decimal | None] = mapped_column (Text, nullable=True)\n")
#     else:
#         for line in keys:
#             file.write(f"{line}: Mapped[Decimal | None] = mapped_column (Numeric(18, 2))\n")

# Convert to Schema
# with open(f'{filename}_schema.json','w') as file:
#     if filename.startswith('tmbctc'):
#         for line in keys:
#             file.write(f'{line}: str | None = None\n')
#     else:
#         for line in keys:
#             file.write(f'{line}: float | None = None\n')
#
# Convert to Alembic
with open(f'{filename}_alembic.json','w') as file:
    if filename.startswith('tmbctc'):
        for line in keys:
            file.write(f'op.add_column(\'{table_name}\', sa.Column(\'{line}\', sa.Text(), nullable=True))\n')
    else:
        for line in keys:
            file.write(f'op.add_column(\'{table_name}\', sa.Column(\'{line}\', a.Numeric(precision=18, scale=2), nullable=True))\n')


# model: --------
#       col_name: Mapped[Decimal | None] = mapped_column(Numeric(18, 2))
#   tmbctc:
#       col_name: Mapped[str] = mapped_column(Text, nullable=True)
#
#
# schema: ---------
#       col_name: float | None = None
#   tmbctc:
#       col_name: str | None = None
#
#
# alembic: ----------
#   tmbctc:
#       op.add_column(table_name, sa.Column(col_name, sa.Text(), nullable=True))
#   others:
#       op.add_column(table_name, sa.Column(col_name, a.Numeric(precision=18, scale=2), nullable=True))
