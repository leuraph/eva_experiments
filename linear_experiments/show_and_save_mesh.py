from p1afempy.mesh import show_mesh
from load_save_dumps import load_dump
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import cm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True,
                        help="path to the mesh files")
    args = parser.parse_args()

    base_path = Path(args.path)
    path_to_coordinates = base_path / 'coordinates.pkl'
    path_to_elements = base_path / 'elements.pkl'
    path_to_solution = base_path / 'galerkin_solution.pkl'

    coordinates = load_dump(path_to_dump=path_to_coordinates)
    elements = load_dump(path_to_dump=path_to_elements)
    galerkin_solution = load_dump(path_to_dump=path_to_solution)

    n_dof = int(base_path.parts[-1])
    parameter_string = base_path.parts[-2]
    experiment_string = base_path.parts[-3]

    output_path_dir = Path(f'plots/{experiment_string}/')
    output_path_name = output_path_dir / f'{parameter_string}_n-dof-{n_dof}.pdf'
    output_path_dir.mkdir(parents=True, exist_ok=True)

    show_mesh(
        coordinates=coordinates,
        elements=elements,
        path_to_save=output_path_name)


if __name__ == '__main__':
    main()
