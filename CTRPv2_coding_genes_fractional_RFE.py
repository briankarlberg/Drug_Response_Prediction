import pandas as pd
import time
from sklearn.svm import SVR
from sklearn.feature_selection import RFE
import argparse

parser = argparse.ArgumentParser(
    description = 'Drug index'
)

parser.add_argument(
    'drug_frame_index',
    type = int,
    help = 'Input drug frame index number'
)

args = parser.parse_args()

dummy_loop = [0]

for i in dummy_loop:

    drug_frame_index = args.drug_frame_index

    file_read_start = time.time()

    coding_genes_CCLE = pd.read_csv(
        './data/coding_genes_CCLE.tsv',
        sep = '\t',
        index_col = 0
    )

    gexp_cell_lines = coding_genes_CCLE.index

    CTRPv2 = pd.read_csv(
        './data/drug_response_CTRPv2.tsv',
        sep = '\t',
        index_col = 'Cell_line'
    )

    CTRPv2_unique_compounds = CTRPv2.Drug.unique()

    multiple_responses = []
    for drg in CTRPv2_unique_compounds:
        drug_frame = CTRPv2[
            CTRPv2.Drug == drg
        ]

        if len(drug_frame.index.unique()) != len(drug_frame):
            multiple_responses.append(drg)

    CTRPv2 = CTRPv2[
        CTRPv2.Drug.isin(
            multiple_responses
        ) == False
    ]

    CTRPv2_unique_compounds = CTRPv2.Drug.unique()

    compound = CTRPv2_unique_compounds[
        drug_frame_index
    ]

    drug_frame = CTRPv2[
        CTRPv2.Drug == CTRPv2_unique_compounds[
            drug_frame_index
        ]
    ]

    drug_frame_cell_lines = drug_frame.index

    cell_line_intersection = gexp_cell_lines.intersection(
        drug_frame_cell_lines
    )

    X = coding_genes_CCLE[
        coding_genes_CCLE.index.isin(
            cell_line_intersection
        )
    ].iloc[:, 2:]

    del(coding_genes_CCLE)

    y = drug_frame[
        drug_frame.index.isin(
            cell_line_intersection
        )
    ].Response

    estimator = SVR(kernel="linear")
    RFE_start_time = time.time()
    selector = RFE(
        estimator,
        n_features_to_select=10,
        step=.5
    )

    RFE_step = '50%'

    selector = selector.fit(X, y)

    out = pd.concat(
        [drug_frame[
            drug_frame.index.isin(
                cell_line_intersection
                )
            ],
        X.loc[
            :, selector.support_
            ]
        ], axis = 1
    )

    end_time = time.time() - RFE_start_time

    out.to_csv(
        'CTRP_features/selected_features/selected_features_' + compound + '_' + str(
            round(
                end_time, 2
            )
        ) + '_' + RFE_step + '_step.tsv',
        sep = '\t',
    )

    print('done')